import pytest
from scripts.deploy import deploy_nft
from scripts.helpful_scripts import get_account
from brownie import exceptions, BasicNFT_Priced


def test_deploy():
    deploy_nft(BasicNFT_Priced)
    nft = BasicNFT_Priced[-1]
    assert nft is not None


def test_priced_good():
    deploy_nft(BasicNFT_Priced)
    nft = BasicNFT_Priced[-1]
    account = get_account()
    nft.safeMint({"from": account, "value": 2 * 10 ** 18})
    assert nft._tokenIdCounter() > 0


def test_priced_bad():
    deploy_nft(BasicNFT_Priced)
    nft = BasicNFT_Priced[-1]
    account = get_account()
    with pytest.raises(exceptions.VirtualMachineError):
        nft.safeMint({"from": account})
