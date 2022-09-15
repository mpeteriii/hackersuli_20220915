from brownie import *

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

# Deploy contract with deployer
contract_tickets = deployer.deploy(Tickets)

# Create snapshot
chain.snapshot()

# Initialize contract with deployer
price = Wei("0.1 ether")
tickets = 100
duration = WEEK
contract_tickets.initialize(price,tickets,duration, {'from': deployer})

# Get user1 ether balance 
user1.balance()

# Buy 3 tickets with user1
ticket_price = 3 * price
contract_tickets.buy(3, {'from': user1, 'value' : ticket_price})

# Refund 1 ticket with user1
contract_tickets.refund(1, {'from': user1})

# Wait 1 week 
chain.sleep(WEEK)
chain.mine(1)

# Withdraw funds with owner
balance = contract_tickets.balance()
contract_tickets.withdraw(balance, {'from': deployer})

# Get user1 ether balance 
user1.balance()

# Get deployer ether balance 
deployer.balance()
