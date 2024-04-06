from brownie import accounts, FundMe, network, config, MockV3Aggregator
from scripts.helpfullscripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOACKCHAIN_ENVIORMENTS,
)
from web3 import Web3


def deploy_fundme():
    account = get_account()
    if network.show_active() not in LOCAL_BLOACKCHAIN_ENVIORMENTS:
        print(network.show_active())
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    print(f"contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fundme()
