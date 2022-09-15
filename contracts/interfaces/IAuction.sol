// SPDX-License-Identifier: ISC
pragma solidity 0.7.4;

interface IAuction  {
    function withdraw() external;

    function bid() external payable;
}