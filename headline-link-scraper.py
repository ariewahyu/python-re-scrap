from bs4 import BeautifulSoup
import requests
url = 'http://timesofindia.indiatimes.com'
htmltext=requests.get(url).text

soup = BeautifulSoup(htmltext)
breaking_news_array= []
for a in soup.findAll('a'):
	if ("new_tops" in str(a) and "liveblog" not in str(a))  or "new_headline" in str(a): 
		if "http://timesofindia.indiatimes.com"+a.get('href') not in breaking_news_array:
			breaking_news_array.append("http://timesofindia.indiatimes.com"+a.get('href'))
print breaking_news_array