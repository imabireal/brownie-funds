from brownie import FundMe
from scripts.helpfullscripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrancefee = fund_me.getEntranceFee()
    print(entrancefee)
    print(f"Current entrance fee is {entrancefee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrancefee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
