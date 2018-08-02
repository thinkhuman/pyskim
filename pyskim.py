
# You must have the Beautiful Soup 4 and requests modules installed.

# Import useful modules to make life easier.
from bs4 import BeautifulSoup
import requests

# Ask the user for a URL to scrape.
url = input("Please enter a website to extract the URLs from: ")
results_file = input("Please enter a name for the file where we'll store the results: ")

# Combine the http request and the user's input, and assign it to r.
r  = requests.get("http://" + url)

# Convert the html into readable text.
data = r.text

# Passs the now readable text to Beautiful Soup, to work its magic.
soup = BeautifulSoup(data)

# Open a text file to write all the links to.
file = open(results_file, "w")

# Using the Beautiful Soup-ed input, find all the 'a' elements, then get and print the link associated with each one.
print ("Alright, here are all the links:\n")

for link in soup.find_all('a'):
	print (link.get('href'))
	file.write(str(link.get('href'))+"\n")

# Close the file containing the links.
print ("\nAll done. The links I found are in a file named {}.".format(results_file))
file.close()
