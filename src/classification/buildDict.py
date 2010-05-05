def buildDict(line,dict):
	line = line.split(' ')
	for word in line:
		if word in dict:
			dict[word] += 1
		else:
			dict[word] = 1
	return dict
dict={}
file = open("../../DB/nonPunc/nonPuncSmiley",'r')
content = file.read()
file.close()
lines = content.splitlines()
for line in lines:
	dict = buildDict(line,dict)

dictfile = open("DICTgood",'w')
for key in dict:
	dictfile.write(key+' '+str(dict[key])+'\n')
dictfile.close()

dict={}
file = open("../../DB/nonPunc/nonPuncFrowny",'r')
content = file.read()
file.close()
lines = content.splitlines()
for line in lines:
	dict = buildDict(line,dict)

dictfile = open("DICTbad",'w')
for key in dict:
	dictfile.write(key+' '+str(dict[key])+'\n')
dictfile.close()
