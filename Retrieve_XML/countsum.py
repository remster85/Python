import urllib
import xml.etree.ElementTree as ET

address = 'http://python-data.dr-chuck.net/comments_327020.xml'

print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

sum=0
results = tree.findall('.//count')

for item in results:
    print item.text
    sum = sum + int(item.text)
    print sum

print sum

