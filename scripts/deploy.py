from brownie import network, BasicNFT, config
from scripts.helpful_scripts import get_contract, get_publish_account


def deploy_nft():
    # Get Account
    publish_account = get_publish_account()
    print(f"Account {publish_account}")

    # configure dependencies
    print(f"The active network is {network.show_active()}")

    print("Deploying BasicNFT")
    nft_contract = BasicNFT.deploy(
        {"from": publish_account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Deployed: {nft_contract}")
    return nft_contract


def main():
    deploy_nft()
