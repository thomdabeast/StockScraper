#! /usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib
import re

stockname = ""

while stockname != 'exit':
  stockname = raw_input("Enter a stock ticker to get the low down or type exit to exit\n")

  if stockname == 'exit':
    break;

  htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s="+stockname+"&ql=1")
  htmltext = htmlfile.read()
  regex = '<div class="bd">(.+?)</div>'
  pattern = re.compile(regex)

  try:
    links = re.findall(pattern, htmltext)[4] #Grab the <div> with Headline News links
   # print links

  except:
    print "Something went horribly wrong."

  links = links.split("a href=\"") #Split to make finding the url link easier
  links.pop(0) # pop the ugly <lu><li> tags
  #for i in links:
   # print i, '\n'

  linklist = []
	#TODO:
  #Make Dictionary for all links found in html
  #Read each character into the correct dictionary bucket until the '"' character is read
  for link in links:
		currlink = ""
		for i in link:
		  if i !='"':
		    currlink += i
		  else:
		    break
		linklist.append(currlink)

  for i in linklist:
    print i, '\n'
  
#links = BeautifulSoup(links)
#for link in links.find_all("ul"):
#  print link
  

#for link in soup.find('div', class="bd"):
#    print link.get('li')
