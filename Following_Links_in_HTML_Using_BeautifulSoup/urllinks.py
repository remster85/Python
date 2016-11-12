# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

maxIterations = 0

def gotolink(url, urlPosition, currentIteration):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    urlNumber = 0
    for tag in tags:
        url =  tag.get('href', None)
        urlNumber = urlNumber + 1
        if currentIteration == maxIterations:
            break
        if urlNumber == urlPosition:
            print url
            gotolink(url, urlPosition, currentIteration+1)
            break


maxIterations = 7
url = 'http://python-data.dr-chuck.net/known_by_Avah.html'
gotolink(url,18,0)

