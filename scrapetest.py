from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(),'lxml')
print(bs.body)
