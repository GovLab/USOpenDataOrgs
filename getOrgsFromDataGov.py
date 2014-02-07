import json  # Import the library that lets us work with JSON
import csv   # Import the library that lets us read/write CSVs
import time 
import urllib2
from bs4 import BeautifulSoup

csvwriter = csv.writer(open("organizations_datagov.csv", "w"))
csvwriter.writerow(["agency", "url", "datasets"])

total_pages = 11
baseURL ='http://catalog.data.gov/organization?page='

for i in range(1, total_pages):
	print "Fetching " +  baseURL + str(i)
	page = urllib2.urlopen(baseURL+str(i))
	soup = BeautifulSoup(page)
	datasets = soup.findAll('li', {"class":"media-item"})
	for d in datasets:
		agency = d.find("h3", {'class':'media-heading'}).string
		url = 'http://catalog.data.gov' + d.find("a", href=True)['href']
		dsets = d.find(attrs={"class":"count"}).string.replace(" Datasets", "")
		newrow = [agency, url, dsets]
		for i in range(len(newrow)):  # For every value in our newrow
			if hasattr(newrow[i], 'encode'):
				newrow[i] = newrow[i].encode('utf8')
		print newrow
		csvwriter.writerow(newrow)



