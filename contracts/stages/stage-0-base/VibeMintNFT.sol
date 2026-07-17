// SPDX-License-Identifier: MIT
pragma solidity ^0.8.31;

import "@openzeppelin/contracts@5.1.0/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts@5.1.0/access/Ownable.sol";
import "@openzeppelin/contracts@5.1.0/utils/Strings.sol";

/// @title VibeMintNFT — Stage 0: ERC-721 base skeleton
/// @notice Educational contract for vibe-mint workshop. Sepolia testnet only.
contract VibeMintNFT is ERC721, Ownable {
    using Strings for uint256;

    uint256 public constant maxSupply = 100;
    uint256 private _totalMinted;
    string private _baseTokenURI;

    constructor() ERC721("VibeMint", "VMINT") Ownable(msg.sender) {}

    function totalMinted() external view returns (uint256) {
        return _totalMinted;
    }

    function setBaseURI(string calldata baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        _requireOwned(tokenId);
        return bytes(_baseTokenURI).length > 0
            ? string(abi.encodePacked(_baseTokenURI, tokenId.toString()))
            : "";
    }
}
