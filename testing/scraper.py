# import libraries
import urllib.request
from bs4 import BeautifulSoup

# specify the url
index_page = "http://172.20.10.11/html/testing/"

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(index_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, ‘html.parser’)

data = soup.find('pre', attrs={'class': 'output'})

beta = data.text.strip() # strip() is used to remove starting and trailing

print beta

# Take out the <div> of name and get its value
# name_box = soup.find('h1', attrs={'class': 'name'})

# name = name_box.text.strip() # strip() is used to remove starting and trailing
# print name

# # get the index price
# price_box = soup.find('div', attrs={'class': 'price'})
# price = price_box.text
# print price