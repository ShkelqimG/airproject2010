#!/usr/bin/python
from svmutil import *
import pickle

print "loading dictionary..."
# load dictionary
dictfile = open("/home/huninghang/workspace/twitterSenti/src/classification/svm/DICT")
dict = pickle.load(dictfile)
dictfile.close()
"Done"
num = 9
stepsize = 1
# try different number of features
while num < 20000:
	stepsize = stepsize * 2
	num = num + stepsize
	print "num =",num
	# preprocess dictionary - delete low frequency words
	deList = []
	for key in dict:
		if dict[key] in range(1,num+1):
			deList.append(key)
	for item in deList:
		del dict[item]
	
	# prepare word index
	i = 1
	idx = {}
	for key in dict:
		idx[key] = i
		i += 1
	print len(dict)
	
	print "loading train set..."
	# load twitter data base
	file = open("/home/huninghang/workspace/twitterSenti/DB/trainset/Step3.rmPUNC",'r')
	linesTrain = file.read().splitlines()
	file.close()
	#print "Done"
	
	#print "loading test set..."
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
			wordIdx = idx[word]
			xi[wordIdx] = 1
		x.append(xi)
	
	param = '-s 1 -t 0'
	print "Training! Nr:",num,param 
	m = svm_train(y[0:len(linesTrain)],x[0:len(linesTrain)],param)
	#file = open("model"+str(fileNr),'w')
	#svm_save_model(file.name,m)
	#file.close()
	print "Training Done!"
		#m = svm_load_model('/result_models/SVMmodel2')
	print "Classifying"
	p_label,p_acc,p_val = svm_predict(y[len(linesTrain):],x[len(linesTrain):], m)
	print "Classification Done!"
	file = open(param,'a')
	file.write(str(num)+";"+str(p_acc)+'\n')	
	file.close()
