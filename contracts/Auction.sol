// SPDX-License-Identifier: ISC
pragma solidity 0.7.4;

import "./interfaces/IERC721.sol";

contract Auction {

    address public owner;
    address public asset;
    uint256 public price;
    uint256 public minbid;
    uint256 public closed;
    address public winner;
    uint256 public assetid;

    mapping(address => uint256) private purchased;

    modifier onlyOwner() {
        require(msg.sender == owner, "Hacker detected!!!");
        _;
    }

    constructor() public {
        owner = msg.sender;
    }

    function initialize(address _asset, uint256 _asssetid, uint256 _minbid, uint256 sale_duration) external onlyOwner {
        minbid = _minbid;
        asset = _asset;
        assetid = _asssetid;
        closed = block.timestamp + sale_duration;
        winner = msg.sender;
        IERC721(asset).transferFrom(msg.sender, address(this), assetid);
    }

    function bid() external payable {
        require(block.timestamp < closed , "Auction was ended!");
        require(msg.value - price >= minbid, "Too small bid!");

        (bool refunded, ) = msg.sender.call{value: price}("");

        winner = msg.sender;
        price = msg.value;
    }

    function withdraw() external {
        require(closed<block.timestamp, "Auction is not over yet!");
        IERC721(asset).transferFrom(address(this), winner, assetid);
    }

}