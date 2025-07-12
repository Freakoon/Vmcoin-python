import datetime
import re
import json
from string import ascii_lowercase,digits,ascii_uppercase
from random import choice,randint

class Store:
	def __init__(self):
		self.file = __file__
	def store(self,data):
		#step 1 get code string
		file_string = None
		with open(self.file,"r") as f:
			file_string = f.read()
		#step 2 get start and end data var
		s = re.finditer(r'\bDa\w*', file_string)
		for m in s:
			pass
		l = file_string[m.start():file_string.rfind('"""')+3]
		#step 3 paste info
		result = ""
		for line in l.splitlines():
			if line == "":
				result += f",{data}\n\n"
			result += line
		#step 4 store in the file
		with open(self.file,"w") as f:
			new = file_string[:m.start()] + result + file_string[file_string.rfind('"""')+3:]
			f.write(new)
	#restore
	def restore(self):
		file_string = None
		with open(self.file,"r") as f:
			file_string = f.read()
		s = re.finditer(r'\bDa\w*', file_string)
		for m in s:
			pass
		l = file_string[m.start():file_string.rfind('"""')+3]
		r = l.replace("\n","")
		result = ""
		inside = None
		for i in r:
			if i == "}":
				result += i
				break
			if i == "{":
				inside = True
				result += i
			elif inside:
				result += i
		return eval(result)
			
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

Data = """{0:0,"233798165326235791970867392620460237432":"VMEviHx","54415630536883040734162628912373286838":"VMpuwnE","3092565169590038264924237000465120465120":"VMmHDOO"

}"""