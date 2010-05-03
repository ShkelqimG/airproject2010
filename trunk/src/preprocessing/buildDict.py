import pickle

def buildDict(line,dict):
	line = line.split(' ')
	for word in line:
		line
		if word in dict:
			dict[word] += 1
		else:
			dict[word] = 1
	return dict

file = open("nonPuncSmiley",'r')
content = file.read()
file.close()
file = open("nonPuncSmiley",'r')
content = content + file.read()
file.close()
lines = content.split('\n')
dict = {}

for line in lines:
	dict = buildDict(line,dict)

dictfile = open("DICTtotal",'w')
pickle.dump(dict,dictfile)
dictfile.close()

printFile = open("print.txt",'w')
for key in dict:
	printFile.write(key+' '+str(dict[key])+'\n')
printFile.close()	
