#! /usr/bin/python

import urllib
import re

stockname = ""
file = open('stockdata.csv', 'w')


while stockname != 'exit':
	stockname = raw_input('Enter a stock ticker to get it\'s price: ')
	if stockname == 'exit':
		break;
	htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s="+stockname+"&ql=1")

	htmltext = htmlfile.read()

	regex = '<span id="yfs_l84_'+stockname+'">(.+?)</span>'
	pattern = re.compile(regex)


	try:
		price = re.findall(pattern,htmltext)	
		price = str(price).split("\'", 2)[1]
			
		file.write(stockname + ",")
		file.write(price + ',')
		file.write('\n')

		print stockname+' price: '+price, '\n'

	except:
		print stockname + " is not a valid ticker", '\n'

file.close()

