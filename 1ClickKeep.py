import pandas as pd
import streamlit as st
import time
import paramiko
from streamlit import components
import paramiko
import io


st.title('KEEP ECDSA+BEACON')

#ETH = st.text_input("Номер локации")
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
#st.write(first_name)
st.markdown('<font color=‘black’>To continue, you need to create a MEW and VPS</font>', unsafe_allow_html=True)


#ETH = st.text_input('Enter ETH adress')
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
        # print(data)
    except Exception:
        #s = st.markdown('<font color=‘orange’>Try again please check pass 1</font>', unsafe_allow_html=True)
        a=0
        st.error('Try again please check user/pass or ip')

    else:
        f.append(client.connect)

        #st.markdown('<font color=‘Black’>Congratulation</font>', unsafe_allow_html=True)
        st.success('Confirmed')

        h = '-h'
        commands = [
            "ls -a"
        ]
        for command in commands:
            #st.write("=" * 30, command, "=" * 30)
            stdin, stdout, stderr = client.exec_command(command)
            a = 1
            #st.write(stdout.read().decode())
            err = stderr.read().decode()
            #st.write(a)
            # if err:
            #     st.write('try')
            # else:
            #     st.write("try again")
        client.close()

    if a==1:
        import json
        #st.write(a)
        #st.set_option('deprecation.showfileUploaderEncoding', False)

        file = st.file_uploader(label="Import (mew) json file (-UTC-)")
        if file:
            file_2 = json.load(file)
            json_string = json.dumps(file_2)

            lll = str(file_2)
            #st.write(json_string)
            #st.write(type(lll))
            #file_1 = file_2.read()
            dictList = []
            for key, value in file_2.items():
                print(value)
                dictList.append(value)
            f = dictList[2]
            st.write(dictList)
            ETH = str('0x') + f
            st.success(ETH)
            #st.write(lll)
        if file:
            pass_eth = st.text_input('Enter password(Wallet JSON)', type="password")
            p = []
            if file and pass_eth:
                from web3.auto import w3

                try:
                    private_key = w3.eth.account.decrypt(file_2,
                                                         pass_eth)
                except:
                    st.error('Try again please check pass for wallet')
                else:
                    st.success('Confirmed')
                    p.append(private_key)
                    if st.button('Run'):
                        #st.write ('GO')
                        client = paramiko.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        client.connect(hostname=host, username=user, password=secret, port=port)
                        h = '-h'
                        commands = [
                            "sudo apt update",
                            "yes | sudo apt install git",
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
                        keepnetwork/keep-client:v1.3.0-rc.4 --config /mnt/beacon/config/config.toml start" %pass_eth,
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
                        keepnetwork/keep-ecdsa-client:v1.2.0-rc.5 --config /mnt/ecdsa/config/config.toml start" %pass_eth
                        ]

                        with st.spinner('Wait ... please'):
                            for command in commands:
                                #st.write("-" * 2,command)
                                stdin, stdout, stderr = client.exec_command(command)
                                print(stdout.read().decode())
                                err = stderr.read().decode()
                                if err:
                                    print(err)

                            # print(data)
                            client.close()
                        st.success('Congratulations, the node is up and running! (please check ECDSA logs on the server itself)')
                        st.success('Paste on server: sudo docker logs keep-client -f --since 1m')
                        #ALTERNATIV without SED
                        # ssh = paramiko.SSHClient()
                        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        # ssh.connect(host,  username=user, password=secret)
                        # sftp = ssh.open_sftp()
                        # # sftp.put('/root/keep-nodes/beacon/','data.txt')
                        # # source= 'config.toml'
                        # # destination ='/root/keep-nodes/beacon/config.toml'
                        # # sftp.put(source,destination)
                        # sftp.get('keep-nodes/beacon/config/config.toml', 'config1.toml')
                        # # localpath = 'abc.txt'
                        # # remotepath = '/opt/crestelsetup/patchzip/abc.txt'
                        # # sftp.put(localpath, remotepath)
                        # sftp.close()
                        # ssh.close()
                        # file = open('config1.toml', mode='r')
                        # lines = file.readlines()
                        # file.close()
                        # my_dict = {}
                        # my_list = []
                        # for line in lines:
                        #     line = line.split()
                        #     line = [i.strip() for i in line]
                        #     st.write(line)
