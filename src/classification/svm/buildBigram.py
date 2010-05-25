# create a dictionary
# key - word
# dict[key] - number of occurrences

def buildDict(tweet,dict):
	words = tweet.split(' ')
	for i in range(0,len(words)-1):
		if words[i] in ["USERNAME","URL","EMAIL"]:
			continue
		if words[i+1] in ["USERNAME","URL","EMAIL"]:
			continue
		phrase = words[i] + " " + words[i+1]
		if phrase in dict:
			dict[phrase] += 1
		else:
			dict[phrase] = 1
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

dictfile = open("printBigram",'w')
for key in dict:
	dictfile.write(key+";"+str(dict[key])+"\n")
dictfile.close()
dictfile = open("DICTBigram",'w')
pickle.dump(dict,dictfile)
dictfile.close()
