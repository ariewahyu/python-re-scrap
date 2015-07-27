import urllib
import re
url='http://timesofindia.indiatimes.com/entertainment/english/Bobbi-Kristina-Brown-daughter-of-Whitney-Houston-dies/articleshow/48230996.cms'
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
img_pattern = re.compile('src="http://timesofindia.indiatimes.com(.+?)">')
data=re.findall(img_pattern,htmltext)
for img in data:
	if('jpg' in img):
 		urllib.urlretrieve('http://timesofindia.indiatimes.com'+img,'/home/umangjain/Desktop/'+title+'.jpg')