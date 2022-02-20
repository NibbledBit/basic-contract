from scripts.deploy import deploy_nft
from brownie import BasicNFT


def test_deploy():
    deploy_nft(BasicNFT)
    nft = BasicNFT[-1]
    assert nft is not None
