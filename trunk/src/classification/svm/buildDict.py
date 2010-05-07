# create a dictionary
# key - word
# value - number of occurrences
i = 1
def buildDict(tweet,dict,i):
	words = tweet.split(' ')
	for word in words:
		if word in ['USERNAME','URL','','EMAIL']:
			continue
		elif word in dict:
			dict[word][1] += 1
		else:
			dict[word] = [i,1]
			i += 1
	return dict,i

import pickle

dict = {}
file = open("/home/huninghang/workspace/twitterSenti/DB/trainset/Step3.rmPUNC",'r')
content = file.read()
file.close()
lines = content.splitlines()
for line in lines:
	line = line.split(";;")
	tweet = line[1]
	dict,i = buildDict(tweet,dict,i)

dictfile = open("DICT",'w')
pickle.dump(dict,dictfile)
dictfile.close()

