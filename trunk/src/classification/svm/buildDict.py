# create a dictionary
# key - word
# dict[key] - number of occurrences

def buildDict(tweet,dict):
	words = tweet.split(' ')
	for word in words:
		if word in ['USERNAME','URL','','EMAIL']:
			continue
		elif word in dict:
			dict[word] += 1
		else:
			dict[word] = 1
	return dict

import pickle

dict = {}
file = open("/home/huninghang/workspace/twitterSenti/DB/trainset/Step3.rmPUNC",'r')
content = file.read()
file.close()
lines = content.splitlines()
for line in lines:
	line = line.split(";;")
	tweet = line[1]
	dict = buildDict(tweet,dict)

dictfile = open("print",'w')
for key in dict:
	dictfile.write(key+";"+str(dict[key])+"\n")
dictfile.close()
