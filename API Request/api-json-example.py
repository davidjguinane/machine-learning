import json
import requests

if __name__=="__main__":
	url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=4beab33cc6d65b05800d51f5e83bde1b&artist=Cher&album=Believe&format=json'
	data = requests.get(url).text
	data = json.loads(data)
	print(type(data))
	print(data)
	data['artist']