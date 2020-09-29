import pandas as pd
import streamlit as st
import time
import paramiko
from streamlit import components
import paramiko
import io
import json

st.title('KEEP ECDSA+BEACON')
st.markdown(("""
       <!DOCTYPE html>
       
<style>
html {
  background: #f3ffe6;
  font-family: helvetica;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: red;

  .blue {
    color: #53d9d1;
  }
  .pink {
    color: white;
  }
  .orange {
    color: #eb7132;
  }
  .console {
    border: 1px solid #333;
    border-radius: 3px;
    margin: 2rem;

    box-shadow: 0 0 15px 0px rgba(0, 0, 0, 0.75);
    .top {
      background: #333;
      color: blue;
      text-align: center;
      font-size: 12px;
      padding: 5px;
      .options {
        font-size: 16px;
        float: left;
      }
    }
    .text {
      font-family: courier;
      color: blue;
      font-size: 14px;
      padding: 0.25rem;
    }
  }
}

.typewriter {
  overflow: hidden;
  width: fit-content;
  white-space: nowrap;
  border-right: 0.10em solid #eb7132;
  animation: typing 1s steps(15, end), blink-caret 0.75s step-end infinite;
}
.stTextInput>div>div>input {
    color: #4F8BF9;
}

/* The typing effect */
@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 60%;
  }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
  from,
  to {
    border-color: transparent;
  }
  50% {
    border-color: orange;
  }
}
/* Google Fonts */
@import url(https://fonts.googleapis.com/css?family=Anonymous+Pro);

/* Global */
html{
  min-height: 100%;
  overflow: hidden;
}

.line-1{
    position: relative;
    top: 50%;  
    width: 24em;
    margin: 0 auto;
    border-right: 2px solid rgba(255,255,255,.75);
    font-size: 180%;
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    transform: translateY(-50%);    
}

/* Animation */
.anim-typewriter{
  animation: typewriter 4s steps(44 , end) 1s 1 normal both,
             blinkTextCursor 500ms steps(44) infinite normal;
}
@keyframes typewriter{
  from{width: 0;}
  to{width: 25em;}
}
@keyframes blinkTextCursor{
  from{border-right-color: rgba(255,255,255,.75);}
  to{border-right-color: green;}
}
@import url(https://fonts.googleapis.com/css?family=Khula:700);
body {
  background: lightgreen;
}
.hidden {
  opacity:0;
}
.console-container {
 
  font-family:Khula;
  font-size:4em;
  text-align:center;
  height:200px;
  width:600px;
  display:block;
  position:absolute;
  color:white;
  top:0;
  bottom:0;
  left:0;
  right:0;
  margin:auto;
}
.console-underscore {
   display:inline-block;
  position:relative;
  top:-0.14em;
  left:10px;
}
</style>

<div><p class="line-1 anim-typewriter">KEEP NODE without linux terminal for 1 click :)</p><div>
<div class="console">
  <div class="top"> <span class="options">⦿ ○ ○</span> <span class="title">KEEP ECDSA/BEACON </span></div>
  <div class="tabs"> </div>
  <div class="text">
    <br>[06:24:55] Finished FREE geth Node <span class="pink">'warm-up-hands'</span> after 0.00 s
    <br>[06:24:55] Starting secure<span class="pink">'No DB + Secure '</span>...
    <br> [06:25:14] KEEP_bin <span class="blue">234</span> steps, <span class="blue">234</span> passes, <span class="blue">0</span> failures: <span class="pink">'<font color=‘black’>SUCCESS</font>'</span>
    <br>
    <p class="typewriter"> root@KEEP sudo <span class="pink">  docker run -d</span></p>
    </span>
  </div>
</div>


</html>
<!-- TradingView Widget END -->
        """),unsafe_allow_html=True)
st.markdown('<font color=‘black’>To continue, you need to create a MEW and VPS</font>', unsafe_allow_html=True)
host = st.text_input('Enter ip(host)')
user = st.text_input('Enter user(host)')
secret = st.text_input('Enter password(host)',type="password")
if secret and user:
    f = []
    port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, username=user, password=secret, port=port)
    except Exception:
        a=0
        st.error('Try again please check user/pass or ip')

    else:
        f.append(client.connect)
        st.success('Confirmed')

        h = '-h'
        commands = [
            "ls -a"
        ]
        for command in commands:

            stdin, stdout, stderr = client.exec_command(command)
            a = 1
            err = stderr.read().decode()
        client.close()

    if a==1:
        import json
        file  = st.file_uploader(label="Import (mew) json file (-UTC-)")
        if file:
            file_2 = json.load(file)
            json_string = json.dumps(file_2)
            lll = str(file_2)
            dictList = []
            for key, value in file_2.items():
                print(value)
                dictList.append(value)
            f = dictList[2]
            
            ETH = str('0x') + f
            st.success(ETH)
        if file:
            pass_eth = st.text_input('Enter password(Wallet JSON)', type="password")
            p = []
            if file and pass_eth:
                from web3.auto import w3
                import web3
                from web3 import Web3

                try:
                    private_key = w3.eth.account.decrypt(file_2,
                                                         pass_eth)
                except:
                    st.error('Try again please check pass for wallet')
                else:
                    ropsten_url = "https://ropsten.infura.io/v3/xxxxxxxxxxx"
                    web3 = Web3(Web3.HTTPProvider(ropsten_url))
                    with open('TokenGrant.json') as r:
                        data = json.load(r)
                    abi = data["abi"]
                    address = web3.toChecksumAddress("0xb64649fe00f8Ef5187d09d109C6F38f13C7CF857")
                    contract = web3.eth.contract(address=address, abi=abi)
                    grand = contract.functions.getGrants(web3.toChecksumAddress(ETH)).call()
                    #st.write(grand)
                    if not grand:
                        st.error('Grand not received go https://us-central1-keep-test-f3e0.cloudfunctions.net/keep-faucet-ropsten?account=%s' % ETH)
                    else:
                        st.success('Grand received')

                    stake = contract.functions.stakeBalanceOf(web3.toChecksumAddress(ETH)).call()
                    if stake != 0 and stake > 90000:
                        st.success('KEEP Tokens delegated')
                    else:
                        st.error('Please delegate KEEP go https://dashboard.test.keep.network/tokens/delegate')

                    with open('KeepRandomBeaconOperator.json') as r:
                        data = json.load(r)
                    abi = data["abi"]
                    address = web3.toChecksumAddress("0xC8337a94a50d16191513dEF4D1e61A6886BF410f")

                    contract = web3.eth.contract(address=address, abi=abi)
                    minstake = contract.functions.hasMinimumStake(web3.toChecksumAddress(ETH)).call()
                    if minstake == True:
                        st.success('Keep Random Beacon Operator Contract Authorized successful')
                    else:
                        st.error('Please Authorize on Keep Random Beacon Operator Contract go https://dashboard.test.keep.network/applications/random-beacon')

                    with open('BondedECDSAKeepFactory.json') as r:
                        data = json.load(r)
                    abi = data["abi"]
                    address = web3.toChecksumAddress("0x9EcCf03dFBDa6A5E50d7aBA14e0c60c2F6c575E6")
                    contract = web3.eth.contract(address=address, abi=abi)
                    KeepFactory = contract.functions.isOperatorAuthorized(web3.toChecksumAddress(ETH)).call()
                    if KeepFactory == False:
                        st.error('Please authorize ECDSAKeepFactory contracts go https://dashboard.test.keep.network/applications/tbtc')
                    else:
                        st.success('Authorize ECDSAKeepFactory confifm')

                    with open('KeepBonding.json') as r:
                        data = json.load(r)
                    abi = data["abi"]
                    address = web3.toChecksumAddress("0x60535A59B4e71F908f3fEB0116F450703FB35eD8")
                    contract = web3.eth.contract(address=address, abi=abi)
                    wei = contract.functions.unbondedValue(web3.toChecksumAddress(ETH)).call()
                    unbonded_eth = web3.fromWei(wei, 'ether')
                    if unbonded_eth == 0:
                        st.error('Add an amount of ETH to the available balance for Bonding go           https://dashboard.test.keep.network/applications/tbtc')
                    else:
                        st.success('Available ETH for bonding %s ETH (recommend >= 20ETH)' % unbonded_eth)
                    if unbonded_eth != 0 and minstake == True and stake != 0 and stake > 90000 and grand != '' and KeepFactory == True:
                        st.success('Confirmed')
                        p.append(private_key)
                        if st.button('Run'):
                            # st.write ('GO')
                            client = paramiko.SSHClient()
                            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            client.connect(hostname=host, username=user, password=secret, port=port)
                            h = '-h'
                            commands = [
                                "sudo apt update",
                                "yes | sudo apt install git -y",
                                "sudo apt install docker.io curl -y",
                                "sudo systemctl start docker",
                                "sudo systemctl enable docker",
                                "sudo ufw allow 22 && sudo ufw allow 3919 && sudo ufw allow 3920 && yes | sudo ufw enable",
                                "sudo ufw status",

                                "git clone https://github.com/icohigh/keep-nodes.git",
                                "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt" % ETH,
                                "echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt" % pass_eth,
                                "echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json" % json_string,
                                "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
                                "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
                                "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
                                "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
                                "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
                                "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
                                "export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)",
                                "sudo docker run -d \
                            --entrypoint /usr/local/bin/keep-client \
                            --restart always \
                            --volume $HOME/keep-nodes/data:/mnt/data \
                            --volume $HOME/keep-nodes/beacon/config:/mnt/beacon/config \
                            --volume $HOME/keep-nodes/beacon/persistence:/mnt/beacon/persistence \
                            --env KEEP_ETHEREUM_PASSWORD=%s \
                            --env LOG_LEVEL=debug \
                            --name keep-client \
                            -p 3919:3919 \
                            keepnetwork/keep-client:v1.3.0-rc.4 --config /mnt/beacon/config/config.toml start" % pass_eth,
                                "sudo docker run -d \
                            --entrypoint /usr/local/bin/keep-ecdsa \
                            --restart always \
                            --volume $HOME/keep-nodes/data:/mnt/data \
                            --volume $HOME/keep-nodes/ecdsa/config:/mnt/ecdsa/config \
                            --volume $HOME/keep-nodes/ecdsa/persistence:/mnt/ecdsa/persistence \
                            --env KEEP_ETHEREUM_PASSWORD=%s \
                            --env LOG_LEVEL=debug \
                            --name keep-ecdsa \
                            -p 3920:3919 \
                            keepnetwork/keep-ecdsa-client:v1.2.0-rc.5 --config /mnt/ecdsa/config/config.toml start" % pass_eth
                            ]

                            with st.spinner('Wait ... please'):
                                for command in commands:
                                    # st.write("-" * 2,command)
                                    stdin, stdout, stderr = client.exec_command(command)
                                    print(stdout.read().decode())
                                    err = stderr.read().decode()
                                    if err:
                                        print(err)

                                # print(data)
                                client.close()
                            st.success(
                                'Congratulations, the node is up and running! (please check ECDSA logs on the server itself)')
                            st.success('Paste on server: sudo docker logs keep-client -f --since 1m')
                         
                    else:
                        st.error("OOPS")
