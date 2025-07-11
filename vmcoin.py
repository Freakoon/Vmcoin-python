import sqlite3
import SecurHash
import datetime
import os
import time 
import json

if not os.path.exists("entities.json") and not os.path.exists("transactions.json"):
	with open("entities.json","w") as f:
		f.write('{"entities":{}}')
	with open("transactions.json","w") as f:
		f.write('{"transactions":{}}')

#SecurObject
hashKey = {}
sh = SecurHash.Hash(hashKey)

#Wallet manager
class Wallet:
	def __init__(self):
		self.entity = {}
		self._restore()
	def _restore(self):
		with open("entities.json","r") as f:
			self.entity = json.load(f)
	#create new user
	def new(self,i=str,random=None):
		if random:
			key = sh.hashKey("VM",5)
			wallet = sh.hashKey("vm",26)
			self.entity["entities"][wallet] = {"key":key,"wallet":wallet,"balance":0.0,"hashkey":{wallet:key}}
		elif not random and i:
			wallet = sh.hashKey("vm",26)
			key = i
			self.entity["entities"][wallet] = {"key":key,"wallet":wallet,"balance":0.0,"hashkey":{wallet:key}}
		with open("entities.json","w") as f:
			json.dump(self.entity,f,indent=4)
			return True
	def info(self):
		return self.entity

w = Wallet()

#Main class
class BlockChain:
	def __init__(self):
		self.transactions = {"transactions":{}}
		self.users = w.info()
		self._restore()
	def _restore(self):
		with open("transactions.json","r") as f:
			self.transactions = json.load(f)
	#send
	def send(self,key, wallet,user,value):
		if value == 0:
			return None
		balance = self.users["entities"][wallet]["balance"]
		#if wallet is there
		if wallet in self.users["entities"]:
			#if key true
			if self.users["entities"][wallet]["hashkey"][wallet] == key:
				#if money there
				if balance > 0 and balance - float(value) > 0:
					self.users["entities"][wallet]["balance"] -= float(value)
					self.users["entities"][user]["balance"] += float(value)
					self.transactions["transactions"][len(self.transactions["transactions"])+1] = {"from":wallet,"to":user,"amount":value,"time":f"{datetime.datetime.now()}","hash":sh.hashKey("tra",5)}
					with open("entities.json","w") as f:
						json.dump(self.users,f,indent=4)
					with open("transactions.json","w") as f:
						json.dump(self.transactions,f,indent=4)
					print(json.dumps(self.transactions,indent=4))
					return 1
				else:
					return -1

BlockChain = BlockChain()

v = 234.458276

BlockChain.send(key="VM5rYUL",wallet="vmAYg$XldrbS@dEOkeMwTMEtjMjr",user="vmWGG$gql3hSnIitIB95X6ATdKGF",value=v)