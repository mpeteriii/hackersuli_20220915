# INSTALL TOOLS



sudo apt-get update

sudo apt-get upgrade

sudo apt install build-essential dkms linux-headers-$(uname -r)

sudo apt install python3.10-venv



sudo apt install python3-pip

python3 -m pip install --user pipx

python3 -m pipx ensurepath



## nvm + npm install

# sudo apt install nodejs npm

sudo apt install curl 

curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 

nvm install 16.16

nvm alias default 16.16

nvm use 16.16



## Install Yarn

npm install --global yarn



## Install Brownie

pipx install eth-brownie

pipx install eth-brownie==v1.18.2



## Add libs to Brownie

pipx inject eth-brownie pytz yfinance ethereum-gasprice pytest



## Install Ganache

sudo npm install -g ganache-cli@v6.12.2



## From home directory:

npm install --save-dev hardhat



## Install Solc

pip install solc-select

solc-select install 0.8.10

solc-select use 0.8.10





# VSCODE



## Extensions

Solidity Visual Developer

## Ganache + Brownie

alias evm-console='brownie console --network mainnet-fork'

alias evm-ganache='ganache-cli --hardfork istanbul --fork https://mainnet.infura.io/v3/$INFURA_KEY -i 80000000'
