# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import re
import twitter

url = "http://www.fbe.yildiz.edu.tr/duyurular"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
# Look at the parts of a tag
#print 'TAG:',tag
#print 'URL:',tag.get('href', None)
#print 'Contents:',tag.contents[0]
#print 'Attrs:',tag.attrs
    urllink = tag.get('href', None)
    if re.findall("^http://www.fbe.yildiz.edu.tr/duyurular/.*", urllink) != []:
        str1 = tag.contents[0]
        str2 = urllink  
        break


text = "Duyuru Basligi: " + str1 + " " + "Duyuru Linki: " + str2
print text, len(text)

api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')

status = api.PostUpdate(str1 + " >> " + str2)
print(status.text)


