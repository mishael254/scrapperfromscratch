from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print("the server could not be found\n ")
else:
    print("The server successfully found\n")
    bs = BeautifulSoup(html.read(),'lxml')
    print(bs.body)



