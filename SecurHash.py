Data = """
{
0:0

}
"""

import datetime
from string import ascii_lowercase,digits,ascii_uppercase
from random import choice,randint


#object hash
class Hash:
	def __init__(self,data:dict):
		#vars
		self.abc = {" ":0,"@":1000,"$":2000,"&":3000}
		self.num = 0
		self.data = data
		self._config()
	def _config(self):
		#Generate hash algoritm
		for ab in ascii_lowercase:
			self.num += 1
			self.abc[ab] = self.num * randint(self.num,9999)
		for di in digits:
			self.num += 1
			self.abc[di] = self.num * randint(self.num,9999)
		for AB in ascii_uppercase:
			self.num += 1
			self.abc[AB] = self.num * randint(self.num,9999)
	#Create with a string
	def change(self,string):
		final_str = ""
		for i in string:
			if string not in self.data:
				self.data[string] = ""
			self.data[string] += f"{self.abc[i]}"
			final_str += f"{self.abc[i]}"
		return final_str
	#restore hash to string
	def change_reverse(self,int_hash):
			rev = {}
			for k,v in self.data.items():
				rev[v] = k
			return rev[int_hash]

#class generator key
class KeyGenerator:
	def __init__(self):
		self.abc = ["$","@","M"]
		self.date = {}
		self._config()
	#abc
	def _config(self):
		for a in ascii_lowercase:
			self.abc.append(a)
		for b in ascii_uppercase:
			self.abc.append(b)
	#generate with start and length
	def new(self,start,length):
			result = ""
			result += start
			for i in range(0,length):
				result += choice(self.abc)
			return result
			
aa = KeyGenerator()

a = Hash({})
b = a.change(aa.new("vm",5))
print(b)
c = a.change_reverse(b)
print(c)