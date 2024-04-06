from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOACKCHAIN_ENVIORMENTS = ["devlopment", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOACKCHAIN_ENVIORMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    account = get_account()
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks ...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(8, 200000000, ({"from": account}))
    print("Mocks deployed")
