'''Python scrirpt to extract all of the email addresses using regex
'''
import re

f=open('our-people')
text = f.readlines()
pattern=r'mailto:(.*)"'


for i  in text:
    match = re.search(pattern, i)
    if match != None:
        print "Email Address:"+ str(match.group(1))
        
f.close()        
