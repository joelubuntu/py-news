from newsapi import NewsApiClient
import urllib.request,json,sys

#get an country code
user_ip = urllib.request.urlopen('https://api.ipify.org/?format=json')
user_json_value = json.loads(user_ip.read())
req_ip = urllib.request.urlopen('http://ip-api.com/json/' + user_json_value['ip'])
req_ip_json = json.loads(req_ip.read())
country_code = req_ip_json['countryCode'].lower()

newsapi = NewsApiClient(api_key='7458b6f09d3c4e77b1c0b95beeb57ad9')
top_headlines = newsapi.get_top_headlines(language='en',country="in")

for i in range(len(top_headlines['articles'])):
	print('\n'+ '•' + "Title: " + top_headlines['articles'][i]['title'])
	print("Description: " + top_headlines['articles'][i]['description'])
	print("Content: " + top_headlines['articles'][i]['content']+"\n")
	print("Read me: " + top_headlines['articles'][i]['url'])
