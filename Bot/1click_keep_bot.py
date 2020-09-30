import logging
import ipaddress
import json
import paramiko
import asyncssh
from web3.auto import w3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
import addr_check_helper

bot = Bot(token=config.bot_token)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)


class MySSHClient(asyncssh.SSHClient):
    def validate_host_public_key(self, host, addr, port, key):
        return True


class SetupStates(StatesGroup):
    waiting_for_server_address = State()
    waiting_for_server_login = State()
    waiting_for_server_password = State()
    waiting_for_wallet = State()
    waiting_for_wallet_password = State()


kb_cancel = u'\U0000274C Cancel'
kb_setup = u'\U00002699 Setup'

# Emoji codes
emoji_ok = u'\U00002705'
emoji_error = u'\U0001F6AB'
emoji_warn = u'\U000026A0'

setup_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
setup_keyboard.add(types.KeyboardButton(text=kb_setup))
cancel_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
cancel_keyboard.add(types.KeyboardButton(text=kb_cancel))
remove_keyboard = types.ReplyKeyboardRemove()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Hi! I\'ll help you to setup KEEP node on your server. Press "Setup" button to begin',
                         reply_markup=setup_keyboard)


@dp.message_handler(lambda message: message.text == kb_cancel, state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Canceled", reply_markup=setup_keyboard)


@dp.message_handler(lambda message: message.text == kb_setup, state='*')
async def begin_setup(message: types.Message):
    await message.answer('Send me your server IP ...', reply_markup=cancel_keyboard)
    await SetupStates.waiting_for_server_address.set()


@dp.message_handler(state=SetupStates.waiting_for_server_address, content_types=types.ContentTypes.TEXT)
async def add_server_address(message: types.Message, state: FSMContext):
    address = message.text
    try:
        ipaddress.ip_address(address)
    except ValueError:
        await message.answer('%s Address `%s` is invalid. Try again' % (emoji_error, address),
                             parse_mode=types.ParseMode.MARKDOWN)
        return
    await state.update_data(server_address=address)
    await message.answer('... your login ...')
    await SetupStates.waiting_for_server_login.set()


@dp.message_handler(state=SetupStates.waiting_for_server_login, content_types=types.ContentTypes.TEXT)
async def add_server_login(message: types.Message, state: FSMContext):
    await state.update_data(server_login=message.text)
    await message.answer('... and password')
    await SetupStates.waiting_for_server_password.set()


@dp.message_handler(state=SetupStates.waiting_for_server_password, content_types=types.ContentTypes.TEXT)
async def add_server_password(message: types.Message, state: FSMContext):
    await state.update_data(server_password=message.text)
    setup_data = await state.get_data()
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=setup_data['server_address'], username=setup_data['server_login'],
                           password=setup_data['server_password'], timeout=5)
        #stdin, stdout, stderr = ssh_client.exec_command('uname -a')
        #print(stdout.read().decode())
    except Exception:
        import traceback
        logging.info('Can\'t connect to server %s with login {%s} and password {%s} for user %s' %
                     (setup_data['server_address'], setup_data['server_login'], setup_data['server_password'],
                      message.from_user.id))
        logging.info(traceback.format_exc())
        await message.answer('%s Can\'t connect to server. Check your IP, login, password and try again' % emoji_warn,
                             reply_markup=cancel_keyboard)
        await message.answer('Send me your server IP ...', reply_markup=cancel_keyboard)
        await SetupStates.waiting_for_server_address.set()
        return
    await message.answer('Ok. Now upload your wallet file in json format (aka keystore)', reply_markup=cancel_keyboard)
    await SetupStates.waiting_for_wallet.set()


@dp.message_handler(state=SetupStates.waiting_for_wallet, content_types=types.ContentTypes.DOCUMENT)
async def add_wallet(message: types.Message, state: FSMContext):
    file_id = message.document.file_id
    file = await bot.download_file_by_id(file_id)
    try:
        wallet = json.load(file)
    except Exception:
        await message.answer('%s Wrong file type. Try again' % emoji_warn, reply_markup=cancel_keyboard)
        return
    if 'address' not in wallet:
        await message.answer('%s Wrong file format. Try again' % emoji_warn, reply_markup=cancel_keyboard)
    else:
        eth_address = '0x%s' % wallet['address']
        check_result = addr_check_helper.check_all(eth_address)
        if check_result != True:
            await message.answer(check_result[1], reply_markup=cancel_keyboard)
            await message.answer('Upload another wallet or try again with this one after fixing issues',
                                 reply_markup=cancel_keyboard)
            return
        await state.update_data(wallet=wallet)
        await state.update_data(eth_address=eth_address)
        await message.answer('Got it. Your address: `%s`\nAnd, finally, give me password to your wallet' % eth_address,
                             reply_markup=cancel_keyboard, parse_mode=types.ParseMode.MARKDOWN)
        await SetupStates.waiting_for_wallet_password.set()


@dp.message_handler(state=SetupStates.waiting_for_wallet_password, content_types=types.ContentTypes.TEXT)
async def add_wallet_password(message: types.Message, state: FSMContext):
    password = message.text
    setup_data = await state.get_data()
    try:
        w3.eth.account.decrypt(setup_data['wallet'], password)
    except Exception:
        import traceback
        logging.info('Wrong wallet password {%s} for user %s' % (password, message.from_user.id))
        logging.info(traceback.format_exc())
        await message.answer('%s Wrong wallet password. Try again' % emoji_warn, reply_markup=cancel_keyboard)
        return
    await message.answer('Great! Let\'s start the installation', reply_markup=remove_keyboard)
    async with asyncssh.connect(setup_data['server_address'], port=22, client_factory=MySSHClient,
                                username=setup_data['server_login'], password=setup_data['server_password']) as conn:
        logging.info('Begin installation on server %s for user %s' % (setup_data['server_address'], message.from_user.id))
        for command in config.commands:
            if '%s' in command:
                result = await conn.run(command % (setup_data['eth_address'], password, json.dumps(setup_data['wallet'])))
            else:
                result = await conn.run(command)
            logging.debug('Command {%s}. Out: %s' % (command, result.stdout))
            if result.stderr:
                logging.warning('Command {%s}. Err: %s' % (command, result.stderr))
                # await message.answer('Error during installation: `%s`' % result.stderr, reply_markup=setup_keyboard,
                                     # parse_mode=types.ParseMode.MARKDOWN)
                # return
    await message.answer('Congratulations! Your node is up and running.\nYou can check logs by running following '
                         'commands on the server:\nFor Keep Beacon Node: `sudo docker logs keep-client -f --since 1m`\n'
                         'For Keep ECDSA Node: `sudo docker logs keep-ecdsa -f --since 1m`',
                         reply_markup=setup_keyboard, parse_mode=types.ParseMode.MARKDOWN)
    await state.finish()

if __name__ == '__main__':
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s', level=logging.DEBUG,
                        filename=config.log_name, datefmt='%d.%m.%Y %H:%M:%S')
    executor.start_polling(dp, skip_updates=True)
