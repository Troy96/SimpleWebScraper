#import BeautifulSoup
from bs4 import BeautifulSoup

#Read the html file sample.html
sample_file=open('sample.html','r')

page = sample_file.read()

#create an instance of BeautifulSoup to parse document
 soul = BeautifulSoup(page, 'html.parser')

 #look for p tag

 reviews = soul.find_all('p')

 #print each review

 for p in review:
 	print p.get_text()
 	