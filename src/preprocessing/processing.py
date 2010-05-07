import re

def rmDupChar(tweet):
	base = None
	num = 0
	i = 0
	while (i < len(tweet)):
		if tweet[i] == base:
			if num == 2:
				tweet = tweet[:i]+tweet[i+1:]
			elif num < 2:
				num += 1
				i += 1
		else:
			num = 1
			base = tweet[i]
			i += 1
	return tweet

# --------------------------main------------------------------
# training set
#add = "/home/huninghang/workspace/twitterSenti/DB/paper/train.40000.2009.05.25"
# test set
add = "/home/huninghang/workspace/twitterSenti/DB/paper/testdata.manual.2009.05.25"

file = open(add,'r')
lines = file.read().lower().splitlines()
file.close()

# create ID dictionary to remove duplicates			#
dictID = {}
for line in lines:
	line = line.split(';;')
	ID = line[1]
	if ID in dictID:
		dictID[ID] += 1
	else:
		dictID[ID] = 1
file = open("IDdict",'w')
for key in dictID:
	file.write(key+"---"+str(dictID[key])+"\n")
file.close()

# Step 1: remove duplicate tweets and loop characters #
file = open("Step1.rmDupChar",'w')
for line in lines:
	line = line.split(";;")
	ID = line[1]
	if dictID[ID] > 1:
		print "duplicated item", ID, "is removed"
		continue
	else:
		tweet = line[5]
		label = line[0]
		tweet = rmDupChar(tweet)
		file.write(label+";;"+tweet+"\n")	
file.close()

#--------------------------------------------------------------
# Step 2: replace USERNAME, URL and EMAIL    #
file = open("Step1.rmDupChar",'r')
string = file.read()
file.close()

pattern2 = re.compile('\w+@\w+.[a-zA-Z]{2,4}')
a=pattern2.sub('EMAIL',string)
print "EMAIL done"
pattern1 = re.compile('((?:http|https)://[a-z0-9\/\?=_#&%~-]+(\.[a-z0-9\/\?=_#&%~-]+)+)|www(\.[a-z0-9\/\?=_#&%~-]+){2,}')
b=pattern1.sub('URL',a)
print "URL done"
pattern = re.compile('@([A-Za-z0-9_]+)')
c=pattern.sub('USERNAME',b)
print "USERNAME done"
file = open("Step2.rpUUE",'w')
file.write(c)
file.close()

# -----------------------------------------------------------------
# Step 3: remove punctuation
file = open("Step2.rpUUE",'r')
content = file.read()
lines = content.splitlines()
pattern = re.compile('\W+')
file.close()

file = open("Step3.rmPUNC",'w')
for line in lines:
	line = line.split(";;")
	nwline = re.sub(pattern,' ',line[1])
	file.write(line[0]+";;"+nwline+'\n')
file.close()	
