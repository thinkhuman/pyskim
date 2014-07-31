
# You must have the Beautiful Soup 4 and requests modules installed.

# Import useful modules to make life easier.
from bs4 import BeautifulSoup
import requests

# Ask the user for a URL to scrape.
url = raw_input("Enter a website to extract the URL's from: ")

# Combine the http request and the user's input, and assign it to r.
r  = requests.get("http://" + url)

# Convert the html into readable text.
data = r.text

# Passs the now readable text to Beautiful Soup, to work its magic.
soup = BeautifulSoup(data)

# Open a text file to write all the links to.
file = open("all_the_links.txt", "w")

#url_list = []

# Using the Beautiful Soup-ed input, find all the 'a' elements, then get and print the link associated with each one.
for link in soup.find_all('a'):
	print link.get('href')
	#url_list.append(str(link.get('href')))
	file.write(str(link.get('href'))+"\n")
	#file.write(str(url_list))
	#print url_list

# Once done, close the file containing the links.
file.close()
