import urllib
import time
import io
import json
from BeautifulSoup import BeautifulSoup

def Ticker(ticker):
	prices = []

	while True:
		htmlfile = urllib.urlopen("http://finance.yahoo.com/q?s="+ticker+"&ql=1")

		htmltext = htmlfile.read()
		soup = BeautifulSoup(htmltext)
		
		holder = soup.find(id="yfs_l84_"+ticker)

		price = holder.contents[0]
		
		print ticker + ": " + price

		prices.append((price, time.asctime(time.localtime(time.time()))))
		
		if len(prices) >= 100:
			f = open(ticker + ".json", 'a')
			json.dump(prices, f)
			f.close()
			prices = []

stockname = raw_input("Enter a stock ticker to collect it's price: ")
Ticker(stockname)