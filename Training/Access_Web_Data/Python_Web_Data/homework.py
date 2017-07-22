import urllib2
from BeautifulSoup import *

'''Scraping Numbers from HTML using BeautifulSoup.
In this assignment you will write a Python program similar to http://www.pythonlearn.com/code/urllink2.py.
The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.'''

# Open the web page
response = urllib2.urlopen('http://python-data.dr-chuck.net/comments_327023.html')
html = response.read()

# simplify the HTML code
soup = BeautifulSoup(html)

# Retrieve all of span tags
tags = soup('span')

# Init the sum
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])

print 'The sum of the numbers in the file ' + str(sum)