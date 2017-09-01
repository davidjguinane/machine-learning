import json
import requests

if __name__=="__main__":
	url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&limit=10&api_key=5ffb248b5cb40c9198676e857a347bd5&format=json'
	data = requests.get(url).text
	data = json.loads(data)
	print(type(data))
	print(data)