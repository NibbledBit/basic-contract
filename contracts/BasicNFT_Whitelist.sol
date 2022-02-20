// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract BasicNFT_Whitelist is ERC721, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter public _tokenIdCounter;

    bytes32 public merkleRoot =
        0xe2fdccb46aa5f9c7fad9470dd24b8108f7ca7c28ded94d028915fe9419aa5bae;
    mapping(address => bool) public whitelistClaimed;

    constructor() ERC721("MyToken", "MTK") {}

    function safeMint(address to, bytes32[] calldata _merkleProof)
        public
        payable
    {
        require(!whitelistClaimed[to], "Address has already claimed.");

        bytes32 leaf = keccak256(abi.encodePacked(to));
        require(
            MerkleProof.verify(_merkleProof, merkleRoot, leaf),
            "Invalid proof."
        );

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(to, tokenId);
        whitelistClaimed[to] = true;
    }

    function setMerkleRoot(bytes32 root) public onlyOwner {
        merkleRoot = root;
    }
}
