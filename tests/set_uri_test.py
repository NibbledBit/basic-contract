import pytest
from scripts.deploy import deploy_nft
from scripts.helpful_scripts import get_account
from brownie import exceptions, BasicNFT_SetToken


def test_deploy():
    deploy_nft(BasicNFT_SetToken)
    nft = BasicNFT_SetToken[-1]
    assert nft is not None


def test_set_uri_good():
    deploy_nft(BasicNFT_SetToken)
    nft = BasicNFT_SetToken[-1]
    pub_account = get_account()
    mint_account = get_account(1)

    nft.safeMint({"from": mint_account})
    nft.setTokenUri(0, "testUri", {"from": pub_account})

    assert nft._tokenIdCounter() > 0


def test_set_uri_bad():
    deploy_nft(BasicNFT_SetToken)
    nft = BasicNFT_SetToken[-1]
    mint_account = get_account(1)

    nft.safeMint({"from": mint_account})

    with pytest.raises(exceptions.VirtualMachineError):
        nft.setTokenUri(0, "testUri", {"from": mint_account})
