from brownie import *
import json
import requests

# Etherscan Key for loadContractABIFromAddress
etherscan_key = "FWT7N7HZS5QN4I863A3FS7GYWRGB5BTE92"

def loadContractABIFromAddress(contractName, address):
	url = "https://api.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(str(address),str(etherscan_key))
	r = requests.get(url)
	result = r.json()['result']
	result = result.replace("false", "False")
	result = result.replace("true", "True")
	abi = eval(result.split("\n")[0])
	return Contract.from_abi(contractName, address, abi)

deployer = accounts[0]
user1 = accounts[1]
user2 = accounts[2]
user3 = accounts[3]
user4 = accounts[4]
user5 = accounts[5]
user6 = accounts[6]
user7 = accounts[7]
user8 = accounts[8]
user9 = accounts[9]

HOUR = 3600
DAY = 24 * HOUR 
WEEK = 7 * DAY

contract_BAYC = loadContractABIFromAddress("BoredApeYachtClub", "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D")

# Test data
asset = contract_BAYC
asset_id = 111
minbid = Wei("1 ether")
duration = WEEK

# Get the original owner of the NFT
bayc_owner = contract_BAYC.ownerOf(asset_id)

contract_BAYC.transferFrom(bayc_owner, deployer, asset_id, {'from': bayc_owner})

# Deploy the contract
contract_auction  = deployer.deploy(Auction)

# Approve the transfer of the token
contract_BAYC.approve(contract_auction, asset_id, {'from': deployer})


# Initialize the auction
contract_auction.initialize(asset,asset_id,minbid,duration, {'from':deployer})

# Example bids
contract_auction.bid({'from': user1, 'value' : Wei("4 ether")})

contract_auction.bid({'from': user2, 'value' : Wei("6 ether")})


contract_evil = user3.deploy(Evil)

user3.transfer(contract_evil, "7 ether")

contract_evil.bid(contract_auction,Wei("7 ether"),{'from': user3})

contract_auction.bid({'from': user2, 'value' : Wei("8 ether")})



assert(contract_auction.winner()==user2)

contract_evil.bid(contract_auction,{'from': user3, 'value' : Wei("10 ether")})

contract_auction.bid({'from': user2, 'value' : Wei("11 ether")})