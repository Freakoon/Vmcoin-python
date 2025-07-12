#Example
import json
import SecurHash
from vmcoin import BlockChain,Wallet

wallet = Wallet()
blockchain= BlockChain()
sh = SecurHash.Store()

#create a new token with random key
wallet.new(random=True)

#create a new token with custom key
wallet.new("Test123")

#keys again hash to random number and store in SecurHash lib
#note: hash save in last line in the SecurHash
print(sh.restore())

#show entities
print(json.dumps(wallet.info(),indent=4))

"""
{
    "entities": {
        "vmsUfZM@egLKzVB@EtbXvdvxPYcW": {
            "key": "VMY@yoS",
            "wallet": "vmsUfZM@egLKzVB@EtbXvdvxPYcW",
            "balance": 0.0,
            "hashkey": {
                "vmsUfZM@egLKzVB@EtbXvdvxPYcW": "VMY@yoS"
            }
        },
        "vmWpJhdHOVGHETSdUUAczgHKrc$@": {
            "key": "Test123",
            "wallet": "vmWpJhdHOVGHETSdUUAczgHKrc$@",
            "balance": 0.0,
            "hashkey": {
                "vmWpJhdHOVGHETSdUUAczgHKrc$@": "Test123"
            }
        }
    }
}

"""

#need write key for send 
blockchain.send(key="VMxxxxx",wallet="vmxxxx....",user="vmxxxxxx....",value=10.5)

print(json.dumps(wallet.info(),indent=4))

#remove token
wallet.rem("vmxxxxxx....")


#all file restore in json file