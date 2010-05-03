import twython.core as twython
import time

twitter = twython.setup()

def search(emoticon):
	DB = ""
	keys =["id","from_user_id","text"]
	search_results = twitter.searchTwitter(emoticon,rpp="80",lang="en")
	results = search_results["results"]
	for result in results:
		temp = ""
		for key in keys:
			try:
				temp = temp + str(result[key]) + ";;"
			except UnicodeEncodeError:
				continue
		DB = DB + temp + "\n"
	return DB

#smile_icon = [":)",": )",":-)",":D"]
#frown_icon = [":(",": (",":-("]

# get smile tweets
cnt = 0

file1 = open("smileyDB",'a')
file2 = open("frownyDB",'a')

while True:
	try:		
		DB = search(":)")
		while True:
			errnum = 0
			try:
				file1.write(DB)
				break
			except:
				errnum = errnum + 1
				time.sleep(2)
				print 'err',errnum 
		cnt = cnt + 1
		print 'smile','runtime =',cnt
		time.sleep(2)

		DB = search(":(")
		while True:
			errnum = 0
			try:
				file2.write(DB)
				break
			except:
				errnum = errnum + 1
				time.sleep(2)
				print 'err',errnum 
		cnt = cnt + 1
		print 'frown','runtime =',cnt
		time.sleep(2)
	except:
		time.sleep(20)
		print "error time sleep"
		continue
