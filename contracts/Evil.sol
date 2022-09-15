// SPDX-License-Identifier: ISC
pragma solidity 0.7.4;

import "./interfaces/IERC721.sol";
import "./interfaces/IAuction.sol";

contract Evil {

    address public owner;

    mapping(address => uint256) private purchased;

    modifier onlyOwner() {
        require(msg.sender == owner, "Hacker detected!!!");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function bid(address auction, uint256 _value) external payable{
        IAuction(auction).bid{value: _value}();
    }

    receive() external payable {
        if(msg.sender != owner) {
            revert();
        }
    }

    fallback () external payable
    {
        if(msg.sender != owner) {
            revert();
        }
    }


    function withdraw(address auction,address asset, uint256 assetid) external {
        IAuction(auction).withdraw();
        IERC721(asset).transferFrom(address(this), msg.sender, assetid);
    }

}