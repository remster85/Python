
import urllib.request
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = input('Enter location: ')

url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode("utf-8")
print('Retrieved',len(data),'characters')

try:
    js = json.loads(str(data))
except:
    js = None
    print(data)

#print(json.dumps(js, indent=4))

print('Location : ' , js['results'][0]['formatted_address'])
print('Place ID : ' , js['results'][0]['place_id'])
