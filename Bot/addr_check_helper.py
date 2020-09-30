import json
from web3 import Web3
import config

w3 = Web3(Web3.HTTPProvider(config.web3_provider))

# TokenGrant
grant_contract = w3.eth.contract(address=config.token_grant_address, abi=json.loads(config.token_grant_abi))
# KeepRandomBeaconOperator
random_beacon_contract = w3.eth.contract(address=config.keep_random_beacon_operator_address,
                                         abi=json.loads(config.keep_random_beacon_operator_abi))
# BondedECDSAKeepFactory
ecdsa_contract = w3.eth.contract(address=config.bonded_ecdsa_keep_factory_address,
                                 abi=json.loads(config.bonded_ecdsa_keep_factory_abi))
# KeepBonding
bonding_contract = w3.eth.contract(address=config.keep_bonding_address, abi=json.loads(config.keep_bonding_abi))


def check_grant(address):
    return True if grant_contract.functions.getGrants(w3.toChecksumAddress(address)).call() else (False, \
           'Please receive token grant for this address. Go to https://us-central1-keep-test-f3e0.cloudfunctions.net/keep-faucet-ropsten?account=%s' % address)


def check_delegation(address):
    stake = grant_contract.functions.stakeBalanceOf(w3.toChecksumAddress(address)).call()
    return True if stake and stake > 90000 else (False, \
           'Please delegate at least 90000 KEEP tokens. Go to https://dashboard.test.keep.network/tokens/delegate')


def check_random_beacon_authorized(address):
    return True if random_beacon_contract.functions.hasMinimumStake(w3.toChecksumAddress(address)).call() else (False, \
           'Please Authorize KeepRandomBeaconOperator contract. Go to https://dashboard.test.keep.network/applications/random-beacon')


def check_ecdsa_authorized(address):
    return True if ecdsa_contract.functions.isOperatorAuthorized(w3.toChecksumAddress(address)).call() else (False, \
           'Please authorize ECDSAKeepFactory contract. Go to https://dashboard.test.keep.network/applications/tbtc')


def check_eth_amount(address):
    unbonded_wei = bonding_contract.functions.unbondedValue(w3.toChecksumAddress(address)).call()
    return True if w3.fromWei(unbonded_wei, 'ether') > 0 else (False, \
           'Please add some ETH to the balance available for bonding. Go to https://dashboard.test.keep.network/applications/tbtc')


def check_all(address):
    for result in [check_grant(address), check_delegation(address), check_random_beacon_authorized(address),
                   check_ecdsa_authorized(address), check_eth_amount(address)]:
        if result != True:
            return result
    return True
