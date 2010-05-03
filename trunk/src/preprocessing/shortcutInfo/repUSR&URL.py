import re

file = open("smileyCorr",'r')
str = file.read()
file.close()
pattern = re.compile('@(\S)*')
a=pattern.sub('USERNAME',str)
pattern1 = re.compile('[a-zA-z]+://[^\s]*')
b=pattern1.sub('URL',a)
file = open("SmileyFinal",'w')
file.write(b)
file.close()

