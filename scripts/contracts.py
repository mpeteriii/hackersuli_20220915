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


# USDT addresses
USDT_ADDRESS = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
USDT_WHALE = "0xf977814e90da44bfa03b6295a0616a897441acec"

# Transfer ether
deployer.transfer(USDT_WHALE, "10 ether")


# Deploy contract

contract_hello = deployer.deploy(Hello)


contract_USDT = loadContractABIFromAddress("TetherToken",USDT_ADDRESS)

contract_USDT.transfer(user1, 1000*10**6, {'from':USDT_WHALE})

