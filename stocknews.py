#! /usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib
import re

stockname = "msft"

while stockname != 'exit':
	stockname = raw_input("Enter a stock ticker to get the low down or type exit to exit\n")

	if stockname == 'exit':
		break;

	htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s="+stockname+"&ql=1")
	htmltext = htmlfile.read()

	soup = BeautifulSoup(htmltext)

	# Get the div that contains all the headline news
	headlines = soup.find(id='yfi_headlines')
	headlines =  headlines.contents[1]

	# Get the links
	for l in headlines.findAll('a'):
		link = l['href']
		
		if(link.find(".com") < 0):
			continue
		
		if(link.find("barrons") > 0):
			print "\nBarons:"
			htmlfile = urllib.urlopen(link)
			soup = BeautifulSoup(htmlfile)
			
			for p in soup.findAll('p'):
				print p
				
		elif(link.find("bizjournals") > 0):
			print "\nbizjournals:"
			print link
		elif(link.find("forbes") > 0):
			print "\nforbes:"
			print link
		elif(link.find("thestreet") > 0):
			print "\nthestreet:"
			print link
		elif(link.find("fool") > 0):
			print "\nfool:"
			print link
		elif(link.find("fortune") > 0):
			print "\nfortune:"
			print link
		else:
			print "\nSomething else:"
			print link

    # Yahoo sites: 
    # <div id="yui_3_18_1_1_*************_****">...</div>
    # <div id="yui_3_18_1_1_*************_****">...</div>
    # ...

    # Forbes:
    # <p>...</p>
    # <p>...</p>
    # ...

    #bizjournals
    # <p class="content__segment">...</p>
    # <p class="content__segment">...</p>
    # ...
