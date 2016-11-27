import json
import urllib.request as url

urlresponse = url.urlopen('http://python-data.dr-chuck.net/comments_327024.json')
uh = urlresponse.read().decode("utf-8")

info = json.loads(uh)
#print(info)

sum = 0
for item in info["comments"]:
    #print('count', item["count"])
    sum = sum + int(item["count"])

print('The total sum of comments is ' + str(sum))