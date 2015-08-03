import urllib
import re
from bs4 import BeautifulSoup
import requests
import Image
import MySQLdb
import os

#-----Link scraper start-------
url = 'http://timesofindia.indiatimes.com'
htmltext=requests.get(url).text

soup = BeautifulSoup(htmltext)
breaking_news_links= []
links_title = []
links_content_array = []
for a in soup.findAll('a'):
	#whatever checks you apply here, apply on both sides of 'OR'
	if ("new_tops" in str(a) and "blog" not in str(a) and "slideshow" not in str(a) and "listshow" not in str(a) and "photogallery" not in str(a))  or ("new_headline" in str(a) and "blog" not in str(a) and "slideshow" not in str(a) and "listshow" not in str(a) and "photogallery" not in str(a)): 
		if "http://timesofindia.indiatimes.com"+a.get('href') not in breaking_news_links:
			breaking_news_links.append("http://timesofindia.indiatimes.com"+a.get('href'))
#------Link scraper end--------
print breaking_news_links
error=0
try:
	for url in breaking_news_links:

		htmltext = urllib.urlopen(url).read()
		# bs = BeautifulSoup(htmltext)
		# for tag in bs.findAll('div',{'class':'widget storyContent article'}):
		# 	print tag.contents
		pattern = re.compile('<div class="Normal">(.+?)</div>')
		data = re.findall(pattern,htmltext)
		article=''
		for a in data:
			article+=a
		readalso_pattern = re.compile('<strong>READ ALSO:(.+?)</strong>')
		data = re.findall(readalso_pattern,article)
		for a in data:
			article = article.replace(a,'')
		#removing extraneous tags
		# readalso_pattern = re.compile('<a(.+?)</a>')
		p = BeautifulSoup(article)	
		print p.text.replace('READ ALSO:','').replace('READ ALSO IN HINDI:','')
		print "-------------------------------------------------------------------------------"
except Exception as e:
	print str(e)
