from brownie import network, config, BasicNFT
from scripts.helpful_scripts import get_account


def deploy_nft(contract):
    # Get Account
    publish_account = get_account()
    print(f"Account {publish_account}")

    # configure dependencies
    print(f"The active network is {network.show_active()}")

    print("Deploying BasicNFT")
    nft_contract = contract.deploy(
        {"from": publish_account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Deployed: {nft_contract}")
    return nft_contract


def main():
    deploy_nft(BasicNFT)
