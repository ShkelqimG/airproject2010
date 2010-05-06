from svmutil import *
import pickle

print "loading dictionary"
# load dictionary
dictfile = open("/home/huninghang/workspace/twitterSenti/src/classification/svm/DICT")
dict = pickle.load(dictfile)
"Done"

print "loading twitter dataset"
# load twitter data base
file = open("/home/huninghang/workspace/twitterSenti/DB/training/Step3.rmPUNC",'r')
lines = file.read().splitlines()
print "Done"

# format training data
y = []
x = []
i = 1
for line in lines:
	print "processing Line",i
	label, tweet = line.split(";;")
	words = tweet.split()
	if int(label) == 4:
		label = 1
	elif int(label) == 0:
		label = -1
	y.append(label)
	score = {}
	for word in words:
		if word == "USERNAME" or word == "EMAIL" or word == "URL":
			continue
		dictIdx = dict[word][0]
		score[dictIdx] = 1
	x.append(score)
	i += 1

print "Training!"
m = svm_train(y[:200],x[:200],'-c 4 -b 1')
print "Training Done!"
p_label,p_acc,p_val = svm_predict(y[200:400], x[200:400], m)
print "Classification Done!"

print p_label
print p_acc
print p_val
