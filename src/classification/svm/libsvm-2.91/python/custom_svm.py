#!/usr/bin/python
from svmutil import *
import pickle

print "loading dictionary..."
# load dictionary
dictfile = open("/home/huninghang/workspace/twitterSenti/src/classification/svm/DICT")
dict = pickle.load(dictfile)
dictfile.close()
"Done"

print "loading train set..."
# load twitter data base
file = open("/home/huninghang/workspace/twitterSenti/DB/trainset/Step3.rmPUNC",'r')
linesTrain = file.read().splitlines()
file.close()
print "Done"

print "loading test set..."
# load twitter data base
file = open("/home/huninghang/workspace/twitterSenti/DB/testset/Step3.rmPUNC",'r')
linesTest = file.read().splitlines()
file.close()
print "Done"

# combine trainset and test set
lines = linesTrain + linesTest

print "formating training data..."
# format training data
y = []
x = []
i = 0
for line in lines:
	xi = {}
	# print "processing Line", i
	label, tweet = line.split(";;")
	words = tweet.split()
	label = int(label)
	if int(label) == 4:
		label = 1
	elif int(label) == 0:
		label = -1
	else:
		continue
	y.append(label)
	for word in words:
		if word not in dict:
			continue
		dictIdx = dict[word][0]
		xi[dictIdx] = 1
	i += 1
	x.append(xi)
 

print "Training!"
prob = svm_problem(y[0:40000],x[0:40000])
param = svm_parameter('-c 4 -b 1')
m = svm_train(prob,param)
print "Training Done!"
print "Classifying"
p_label,p_acc,p_val = svm_predict(y[40000:], x[40000:], m)
print "Classification Done!"
print p_label
#print p_label
#print p_acc
#print p_val

