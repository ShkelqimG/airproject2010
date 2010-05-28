import string
import pickle

keywords = {};
posFile = open("pos",'r')
lines = posFile.read().lower().splitlines()
for line in lines:
	keywords[line]=1
posFile.close()

negWds = {};
negFile = open("neg",'r')
lines = negFile.read().lower().splitlines()
for line in lines:
	keywords[line]=-1
negFile.close()

print "key words Done"

db = []
address ="../../../DB/testset/Step3.rmPUNC"
dbfile = open(address,'r')
lines = dbfile.read().splitlines()
for line in lines:
	all = line.split(';;')
	tweet = all[1]
	if all[0] == '0':
		label = -1
	if all[0] == '4':
		label = 1
	if all[0] == '2':
		label = 0
	score = 0
	WORD = []
	for key in keywords:
		count = string.count(tweet,key)
		if count > 0:
			WORD.append([key,count,keywords[key]])
		score = score + keywords[key] * count
	if score > 0:
		result = 1
	elif score < 0:
		result = -1
	else:
		result = 1 
	db.append([label,result,WORD,tweet])
TP=0
FN=0
TN=0
FP=0
file = open("RESULTdb",'w')
pickle.dump(db,file)

for item in db:
	pred = item[1]
	actual = item[0]
	if pred == 1 and actual == 1:
		TP+=1
	elif actual == -1 and pred == 1:
		FP+=1
	elif actual == 1 and pred == -1:
		TN+=1
	elif actual == -1 and pred == -1:
		FN+=1
print TP, FP
print TN, FN
a = (float(TP)+FN)/(float(TP)+TN+FP+FN)
print a
