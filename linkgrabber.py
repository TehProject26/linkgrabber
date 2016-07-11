# Version 1 of a simple url grabber

import re, urllib2
  
#for user to input url
url = raw_input("Whats The URL To Crawl ?: ")

#connect to a URL
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

#to output all urls in new lines
for i in links:
    print(i)

