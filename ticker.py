#! /usr/bin/python
import urllib
import re
import threading
import time
import io
import json
from BeautifulSoup import BeautifulSoup

def Pricer(ticker, cond):
	prices = []

	while not cond.is_set():
		htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s="+ticker+"&ql=1")

		htmltext = htmlfile.read()
		soup = BeautifulSoup(htmltext)
		
		holder = soup.find(id="yfs_l84_"+ticker)

		price = holder.contents[0]

		prices.append((price, time.asctime(time.localtime(time.time()))))
		
		if len(prices) >= 100:
			f = open(ticker + ".json", 'a')
			json.dump(prices, f)
			f.close()
			prices = []
			



stockname = ""
threads = []
while stockname != 'exit':
	stockname = raw_input("Enter a stock ticker to collect it's price: ")
	
	if stockname == 'exit':
		for thread, c in threads:
			c.set()
		print "Exiting..."
		break;
	
	try:
		cond = threading.Event()
		t = threading.Thread(target=Pricer, args=(stockname,cond,))
		threads.append((t, cond))
		t.start()
	except:
		continue