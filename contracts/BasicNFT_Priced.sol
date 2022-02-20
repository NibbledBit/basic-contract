// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract BasicNFT_Priced is ERC721 {
    using Counters for Counters.Counter;

    Counters.Counter public _tokenIdCounter;

    constructor() ERC721("MyToken", "MTK") {
        mintFee = 1 * 10**18;
    }

    uint256 mintFee;

    function safeMint() public payable {
        require(msg.value > mintFee, "Pay X ETH to mint.");

        uint256 change = msg.value - mintFee;
        payable(msg.sender).transfer(change);

        address to = msg.sender;
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }
}
