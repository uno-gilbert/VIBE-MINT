// SPDX-License-Identifier: MIT
pragma solidity ^0.8.31;

import "@openzeppelin/contracts@5.1.0/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts@5.1.0/access/Ownable.sol";
import "@openzeppelin/contracts@5.1.0/utils/Strings.sol";

/// @title VibeMintNFT — Stage 1: public mint + supply cap
contract VibeMintNFT is ERC721, Ownable {
    using Strings for uint256;

    uint256 public constant maxSupply = 100;
    uint256 public constant mintPrice = 0.001 ether;
    uint256 public constant MAX_PER_WALLET = 3;

    uint256 private _totalMinted;
    string private _baseTokenURI;
    mapping(address => uint256) public mintedCount;

    constructor() ERC721("VibeMint", "VMINT") Ownable(msg.sender) {}

    function totalMinted() external view returns (uint256) {
        return _totalMinted;
    }

    function setBaseURI(string calldata baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function mint() external payable {
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_totalMinted < maxSupply, "Max supply reached");
        require(mintedCount[msg.sender] < MAX_PER_WALLET, "Wallet limit reached");

        uint256 tokenId = _totalMinted;
        _safeMint(msg.sender, tokenId);

        unchecked {
            _totalMinted++;
            mintedCount[msg.sender]++;
        }

        uint256 refund = msg.value - mintPrice;
        if (refund > 0) {
            (bool ok, ) = msg.sender.call{value: refund}("");
            require(ok, "Refund failed");
        }
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        _requireOwned(tokenId);
        return bytes(_baseTokenURI).length > 0
            ? string(abi.encodePacked(_baseTokenURI, tokenId.toString()))
            : "";
    }
}
