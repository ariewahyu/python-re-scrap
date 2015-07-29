import urllib
import re
from bs4 import BeautifulSoup
import requests
from PIL import Image
#-----Link scraper start-------
url = 'http://timesofindia.indiatimes.com'
htmltext=requests.get(url).text

soup = BeautifulSoup(htmltext)
breaking_news_array= []
for a in soup.findAll('a'):
	if ("new_tops" in str(a) and "blog" not in str(a) and "slideshow" not in str(a))  or "new_headline" in str(a): 
		if "http://timesofindia.indiatimes.com"+a.get('href') not in breaking_news_array:
			breaking_news_array.append("http://timesofindia.indiatimes.com"+a.get('href'))
#------Link scraper end--------


for url in breaking_news_array:

	htmltext = urllib.urlopen(url).read()
	# bs = BeautifulSoup(htmltext)
	# for tag in bs.findAll('div',{'class':'widget storyContent article'}):
	# 	print tag.contents
	pattern = re.compile('<div class="Normal">(.+?)</div>')
	data = re.findall(pattern,htmltext)
	article=''
	for a in data:
		article+=a#.replace('<strong>','').replace('</strong>','').replace('&nbsp;','').replace('&quot;','').replace('<br>','').replace('<br/>','')
	# print article
	readalso_pattern = re.compile('<a(.+?)</a>')
	data = re.findall(readalso_pattern,article)
	for a in data:
		article = article.replace(a,'')
	if '<img' in article:
		img_pattern = re.compile('<img(.+?)>')
		data = re.findall(img_pattern,article)
		for a in data:
			article = article.replace(a,'')
	print article.replace('<img>','').replace('<a</a>','').replace('<br><br>','<br>').replace('<br> <br>','<br>').replace('READ ALSO','').replace('READ THIS IN HINDI:','')


	#scraping title for that particular article
	tit_pattern=re.compile('<title>(.+?) - The Times of India')
	data=re.findall(tit_pattern,htmltext)
	title=data[0]
	print title
	#scraping image for that particular article
	img_pattern = re.compile('src="http://timesofindia.indiatimes.com(.+?).jpg')
	data=re.findall(img_pattern,htmltext)
	for img in data:
	 		urllib.urlretrieve('http://timesofindia.indiatimes.com'+img+'.jpg','/home/umangjain/Downloads/'+title+'.jpg')
	 		# print('Start-http://timesofindia.indiatimes.com'+img+'.jpg-end')
	 		img = Image.open('/home/umangjain/Downloads/'+title+'.jpg')
	 		img = img.resize((708,350),2)
	 		img.save('/home/umangjain/Downloads/news/img/'+title+'.jpg','JPEG')