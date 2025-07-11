import datetime
from string import ascii_lowercase,digits,ascii_uppercase
from random import choice


#شی هش
class Hash:
	def __init__(self,data:dict):
		#متغیر های لازم از شی
		self.abc = {" ":0,"@":1000,"$":2000,"&":3000}
		self.num = 0
		self.date = {}
		self.data = data
		self._config()
	def _config(self):
		#تابع درست کردن الگوریتم هش
		for ab in ascii_lowercase:
			self.num += 1
			self.abc[ab] = self.num * 11
		for di in digits:
			self.num += 1
			self.abc[di] = self.num * 11
		for AB in ascii_uppercase:
			self.num += 1
			self.abc[AB] = self.num * 11
	#تابع تبدیل رشته به هش عددی
	def change(self,string):
		final_str = ""
		for i in string:
			if string not in self.data:
				self.data[string] = ""
			self.data[string] += f"{self.abc[i]}"
			final_str += f"{self.abc[i]}"
		return final_str
	#تابع برعکس کردن هش به رشته 
	def change_reverse(self,int_hash):
			rev = {}
			for k,v in self.data.items():
				rev[v] = k
			return rev[int_hash]
	#تابع تولید هش بصورت متنی با طول و شروع مشخص 
	def hashKey(self,start,length):
		result = ""
		result += start
		abc = ["$","@","M"]
		for k in self.abc:
			if k == " ":
				continue
			abc.append(k)
		for up in ascii_uppercase:
			abc.append(up)
		for i in range(0,length):
			result += choice(abc)
		return result
	def info(self):
		return self.date
		
class KeyGenerator:
	def __init__(self):
		self.abc = ["$","@","M"]
		self.date = {}
		self._config()
	def _config(self):
		for a in ascii_lowercase:
			self.abc.append(a)
		for b in ascii_uppercase:
			self.abc.append(b)
	def new(self,start,length):
			result = ""
			result += start
			for i in range(0,length):
				result += choice(self.abc)
			return result
			
aa = KeyGenerator()

a = Hash({})
b = a.change("vmAYg$XldrbS@dEOkeMwTMEtjMjr")
print(b)
c = a.change_reverse(b)
print(c)