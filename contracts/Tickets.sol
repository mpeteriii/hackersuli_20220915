// SPDX-License-Identifier: ISC
pragma solidity 0.7.4;

contract Tickets {

    address public owner;
    uint256 public price;
    uint256 public tickets;
    uint256 public closed;

    mapping(address => uint256) private purchased;

    modifier onlyOwner() {
        require(msg.sender == owner, "Hacker detected!!!");
        _;
    }

    function initialize(uint256 _price, uint256 _tickets, uint256 sale_duration) external {
        owner = msg.sender;
        price = _price;
        tickets = _tickets;
        closed = block.timestamp + sale_duration;
    }

    function buy(uint256 quantity) external payable {
        require(price != 0, "Not yet initialized!");
        require(block.timestamp < closed , "Sale was ended!");
        require(msg.value >= quantity * price, "Not enough minerals!!!");
        purchased[msg.sender] += quantity;
    }

    function refund(uint256 quantity) external {
        require(price != 0, "Not yet initialized!");
        require(block.timestamp < closed , "No refound. Sale was ended!");
        require(quantity <= purchased[msg.sender], "You don't have enough tickets!");

        (bool refunded, ) = msg.sender.call{value: quantity * price}("");
        require(refunded, "Ticket refund failed");
        purchased[msg.sender] -= quantity;
    }

    function withdraw(uint256 _value) external onlyOwner {
        require(price != 0, "Not yet initialized!");
        require(closed<block.timestamp, "Sale is not over yet!");
        (bool success, ) = msg.sender.call{value: _value}("");
        require(success, "Not enough minerals!!!");
    }

    receive() external payable {}
}