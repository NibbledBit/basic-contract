import pytest
from scripts.deploy import deploy_nft
from scripts.helpful_scripts import get_account
from brownie import exceptions, BasicNFT_Whitelist


def test_deploy():
    deploy_nft(BasicNFT_Whitelist)
    nft = BasicNFT_Whitelist[-1]
    assert nft is not None


def test_priced_good():
    proof = [
        "0xd8490bd55bfd05ce0e6209f96e3ca523dcadb2375435e63fbab8d7666b451116",
        "0x09ad0ca0b27030ef969a7c4d013e89326e2fcbe3b9e09c4d6edadbab003f56a6",
    ]
    minter = "0xdd74C74Ba0079983A80d2A9Ceb7eFbC95232234e"

    deploy_nft(BasicNFT_Whitelist)
    nft = BasicNFT_Whitelist[-1]
    account = get_account()
    nft.safeMint(minter, proof, {"from": account, "value": 2 * 10 ** 18})
    assert nft._tokenIdCounter() > 0


def test_priced_bad():
    proof = [
        "0xd8490bd55bfd05ce0e6209f96e3ca523dcadb2375435e63fbab8d7666b451116",
        "0x09ad0ca0b27030ef969a7c4d013e89326e2fcbe3b9e09c4d6edadbab003f56a6",
    ]
    minter = "0xdd74C74Ba0079983A80d2A9Ceb7eFbC95232234e"

    deploy_nft(BasicNFT_Whitelist)
    nft = BasicNFT_Whitelist[-1]
    account = get_account()

    with pytest.raises(exceptions.VirtualMachineError):
        nft.safeMint(account, proof, {"from": account, "value": 2 * 10 ** 18})
