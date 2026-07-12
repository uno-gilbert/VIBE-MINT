// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/// @title VibeMintNFT — Complete solution
/// @notice Sepolia testnet educational use only. Professional audit required for mainnet.
contract VibeMintNFT is ERC721, Ownable, Pausable, ReentrancyGuard {
    using Strings for uint256;

    uint256 public constant maxSupply = 100;
    uint256 public constant mintPrice = 0.001 ether;
    uint256 public constant MAX_PER_WALLET = 3;
    uint256 public constant MAX_WHITELIST_BATCH = 200;

    uint256 private _totalMinted;
    string private _baseTokenURI;
    bool public publicMintEnabled = true;

    mapping(address => uint256) public mintedCount;
    mapping(address => bool) public whitelist;

    event WhitelistUpdated(address indexed account, bool allowed);

    constructor() ERC721("VibeMint", "VMINT") Ownable(msg.sender) {}

    receive() external payable {}

    function totalMinted() external view returns (uint256) {
        return _totalMinted;
    }

    function setBaseURI(string calldata baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function setPublicMintEnabled(bool enabled) external onlyOwner {
        publicMintEnabled = enabled;
    }

    function setWhitelist(address[] calldata accounts, bool allowed) external onlyOwner {
        require(accounts.length <= MAX_WHITELIST_BATCH, "Batch too large");
        for (uint256 i = 0; i < accounts.length; ) {
            address account = accounts[i];
            require(account != address(0), "Invalid address");
            whitelist[account] = allowed;
            emit WhitelistUpdated(account, allowed);
            unchecked {
                i++;
            }
        }
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function mint() external payable whenNotPaused {
        require(publicMintEnabled, "Public mint disabled");
        _mintWithPayment(msg.sender, 1);
    }

    function whitelistMint() external payable whenNotPaused {
        require(whitelist[msg.sender], "Not whitelisted");
        _mintWithPayment(msg.sender, 1);
    }

    function ownerMint(address to, uint256 quantity) external onlyOwner whenNotPaused {
        require(to != address(0), "Invalid recipient");
        _mintWithoutPayment(to, quantity);
    }

    function withdraw() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance");
        (bool ok, ) = owner().call{value: balance}("");
        require(ok, "Withdraw failed");
    }

    function _mintWithPayment(address to, uint256 quantity) private {
        require(msg.value >= mintPrice * quantity, "Insufficient payment");
        _mintWithoutPayment(to, quantity);

        uint256 required = mintPrice * quantity;
        uint256 refund = msg.value - required;
        if (refund > 0) {
            (bool ok, ) = msg.sender.call{value: refund}("");
            require(ok, "Refund failed");
        }
    }

    function _mintWithoutPayment(address to, uint256 quantity) private {
        require(quantity > 0, "Zero quantity");
        require(_totalMinted + quantity <= maxSupply, "Max supply reached");
        require(mintedCount[to] + quantity <= MAX_PER_WALLET, "Wallet limit reached");

        for (uint256 i = 0; i < quantity; ) {
            uint256 tokenId = _totalMinted;
            _safeMint(to, tokenId);
            unchecked {
                _totalMinted++;
                i++;
            }
        }
        mintedCount[to] += quantity;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        _requireOwned(tokenId);
        return bytes(_baseTokenURI).length > 0
            ? string(abi.encodePacked(_baseTokenURI, tokenId.toString()))
            : "";
    }
}
