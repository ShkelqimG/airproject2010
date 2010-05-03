# replace words "looooove" by "loove" 

class rmDupChar:
	deleteWds = ""
	def __init__(self):
		for line in open("frowny.txt",'r'):
			line = line.split(";;")
			line = line[5]
			line = line.lower()
			self.rm(line)
		print self.deleteWds
		
	def rm(self,str):
		base = None
		num = 0
		i = 0
		while (i < len(str)):
			if str[i] == base:
				if num >= 2:
					self.deleteWds = self.deleteWds + str[i]
					str = str[:i]+str[i+1:]
				else:
					num += 1
					i += 1
			else:
				num = 1
				base = str[i]
				i += 1
		file = open("frownyCorr",'a')
		file.write(str)
		file.close()
		

