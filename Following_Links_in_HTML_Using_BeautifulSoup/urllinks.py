# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *


def gotolink(url, position, currentIteration, maxIterations): #program does nothing as written
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    times = 0
    for tag in tags:
        url =  tag.get('href', None)
        times = times + 1
        if currentIteration == maxIterations:
            break
        if times == position:
            print url
            gotolink(url, position, currentIteration+1, maxIterations)
            break


url = 'http://python-data.dr-chuck.net/known_by_Avah.html'
gotolink(url,18,0,7)

