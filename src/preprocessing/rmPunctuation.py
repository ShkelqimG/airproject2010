import re

file = open("SmileyFinal",'r')
content = file.read()
lines = content.split('\n')
pattern = re.compile('\W')
file.close()

file = open("nonPuncSmiley",'w')
for line in lines:
	nwline = re.sub(pattern,' ',line)
	file.write(nwline+'\n')
file.close()	
