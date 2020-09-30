bot_token = 'TOKEN'
web3_provider = 'https://ropsten.infura.io/v3/INFURA_ID'
log_name = '1click_keep_bot.log'
commands = [
    "sudo apt update",
    "sudo apt install docker.io curl git -y",
    "sudo systemctl start docker",
    "sudo systemctl enable docker",
    "sudo ufw allow 3919 && sudo ufw allow 3920",
    "sudo ufw status",

    "git clone https://github.com/icohigh/keep-nodes.git",
    "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt && echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt && echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json",
    "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
    "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
    "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
    "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
    "sudo docker run -d \
        --entrypoint /usr/local/bin/keep-client \
        --restart always \
        --volume $HOME/keep-nodes/data:/mnt/data \
        --volume $HOME/keep-nodes/beacon/config:/mnt/beacon/config \
        --volume $HOME/keep-nodes/beacon/persistence:/mnt/beacon/persistence \
        --env KEEP_ETHEREUM_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt) \
        --env LOG_LEVEL=debug \
        --name keep-client \
        -p 3919:3919 \
        keepnetwork/keep-client:v1.3.0-rc.4 --config /mnt/beacon/config/config.toml start",
    "sudo docker run -d \
        --entrypoint /usr/local/bin/keep-ecdsa \
        --restart always \
        --volume $HOME/keep-nodes/data:/mnt/data \
        --volume $HOME/keep-nodes/ecdsa/config:/mnt/ecdsa/config \
        --volume $HOME/keep-nodes/ecdsa/persistence:/mnt/ecdsa/persistence \
        --env KEEP_ETHEREUM_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt) \
        --env LOG_LEVEL=debug \
        --name keep-ecdsa \
        -p 3920:3919 \
        keepnetwork/keep-ecdsa-client:v1.2.0-rc.5 --config /mnt/ecdsa/config/config.toml start"
            ]
token_grant_address = '0xb64649fe00f8Ef5187d09d109C6F38f13C7CF857'
token_grant_abi = '[{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"grantManager","type":"address"},{"indexed":false,"internalType":"address","name":"stakingContract","type":"address"}],"name":"StakingContractAuthorized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"}],"name":"TokenGrantCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"}],"name":"TokenGrantRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"grantId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"operator","type":"address"}],"name":"TokenGrantStaked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"grantId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenGrantWithdrawn","type":"event"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"grantIndices","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"grantStakes","outputs":[{"internalType":"contractTokenGrantStake","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"granteesToOperators","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"grants","outputs":[{"internalType":"address","name":"grantManager","type":"address"},{"internalType":"address","name":"grantee","type":"address"},{"internalType":"uint256","name":"revokedAt","type":"uint256"},{"internalType":"uint256","name":"revokedAmount","type":"uint256"},{"internalType":"uint256","name":"revokedWithdrawn","type":"uint256"},{"internalType":"bool","name":"revocable","type":"bool"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"cliff","type":"uint256"},{"internalType":"uint256","name":"withdrawn","type":"uint256"},{"internalType":"uint256","name":"staked","type":"uint256"},{"internalType":"contractGrantStakingPolicy","name":"stakingPolicy","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"numGrants","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token","outputs":[{"internalType":"contractERC20Burnable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_stakingContract","type":"address"}],"name":"authorizeStakingContract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"stakeBalanceOf","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getGrant","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"withdrawn","type":"uint256"},{"internalType":"uint256","name":"staked","type":"uint256"},{"internalType":"uint256","name":"revokedAmount","type":"uint256"},{"internalType":"uint256","name":"revokedAt","type":"uint256"},{"internalType":"address","name":"grantee","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getGrantUnlockingSchedule","outputs":[{"internalType":"address","name":"grantManager","type":"address"},{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"cliff","type":"uint256"},{"internalType":"address","name":"policy","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_granteeOrGrantManager","type":"address"}],"name":"getGrants","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"grantee","type":"address"}],"name":"getGranteeOperators","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"operator","type":"address"}],"name":"getGrantStakeDetails","outputs":[{"internalType":"uint256","name":"grantId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"stakingContract","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"address","name":"_token","type":"address"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"receiveApproval","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"unlockedAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"withdrawable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"revoke","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"withdrawRevoked","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_stakingContract","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"stake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_grantId","type":"uint256"}],"name":"availableToStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"cancelStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"undelegate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"cancelRevokedStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"undelegateRevoked","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"recoverStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
keep_random_beacon_operator_address = '0xC8337a94a50d16191513dEF4D1e61A6886BF410f'
keep_random_beacon_operator_abi = '[{"inputs":[{"internalType":"address","name":"_serviceContract","type":"address"},{"internalType":"address","name":"_stakingContract","type":"address"},{"internalType":"address","name":"_registryContract","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"memberIndex","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"groupPubKey","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"misbehaved","type":"bytes"}],"name":"DkgResultSubmittedEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beneficiary","type":"address"},{"indexed":false,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"groupIndex","type":"uint256"}],"name":"GroupMemberRewardsWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newEntry","type":"uint256"}],"name":"GroupSelectionStarted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes","name":"groupPubKey","type":"bytes"}],"name":"OnGroupRegistered","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes","name":"previousEntry","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"groupPublicKey","type":"bytes"}],"name":"RelayEntryRequested","type":"event"},{"anonymous":false,"inputs":[],"name":"RelayEntrySubmitted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"groupIndex","type":"uint256"}],"name":"RelayEntryTimeoutReported","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"groupIndex","type":"uint256"}],"name":"UnauthorizedSigningReported","type":"event"},{"constant":true,"inputs":[],"name":"currentRequestGroupIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"currentRequestPreviousEntry","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"currentRequestStartBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"dkgGasEstimate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"dkgSubmitterReimbursementFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"entryVerificationGasEstimate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"gasPriceCeiling","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"groupMemberBaseReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"groupSelectionGasEstimate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"groupSize","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"groupThreshold","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"relayEntryTimeout","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"resultPublicationBlockStep","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"genesis","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"serviceContract","type":"address"}],"name":"addServiceContract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"serviceContract","type":"address"}],"name":"removeServiceContract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_newEntry","type":"uint256"},{"internalType":"addresspayable","name":"submitter","type":"address"}],"name":"createGroup","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"isGroupSelectionPossible","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ticket","type":"bytes32"}],"name":"submitTicket","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ticketSubmissionTimeout","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"submittedTickets","outputs":[{"internalType":"uint64[]","name":"","type":"uint64[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"selectedParticipants","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"submitterMemberIndex","type":"uint256"},{"internalType":"bytes","name":"groupPubKey","type":"bytes"},{"internalType":"bytes","name":"misbehaved","type":"bytes"},{"internalType":"bytes","name":"signatures","type":"bytes"},{"internalType":"uint256[]","name":"signingMembersIndexes","type":"uint256[]"}],"name":"submitDkgResult","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"requestId","type":"uint256"},{"internalType":"bytes","name":"previousEntry","type":"bytes"}],"name":"sign","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes","name":"_groupSignature","type":"bytes"}],"name":"relayEntry","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"isEntryInProgress","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"reportRelayEntryTimeout","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"groupProfitFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"staker","type":"address"}],"name":"hasMinimumStake","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"groupPubKey","type":"bytes"}],"name":"isGroupRegistered","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"groupPubKey","type":"bytes"}],"name":"isStaleGroup","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"numberOfGroups","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"groupPubKey","type":"bytes"}],"name":"getGroupMemberRewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"uint256","name":"groupIndex","type":"uint256"}],"name":"hasWithdrawnRewards","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"uint256","name":"groupIndex","type":"uint256"}],"name":"withdrawGroupMemberRewards","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getFirstActiveGroupIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"groupIndex","type":"uint256"}],"name":"getGroupPublicKey","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"entryVerificationFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"groupCreationFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"groupPubKey","type":"bytes"}],"name":"getGroupMembers","outputs":[{"internalType":"address[]","name":"members","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getNumberOfCreatedGroups","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"groupIndex","type":"uint256"}],"name":"getGroupRegistrationTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"groupIndex","type":"uint256"}],"name":"isGroupTerminated","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"groupIndex","type":"uint256"},{"internalType":"bytes","name":"signedMsgSender","type":"bytes"}],"name":"reportUnauthorizedSigning","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}
