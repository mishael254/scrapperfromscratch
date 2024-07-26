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

    try:
        paragraphOutput = bs.body.div
    except AttributeError as e:
        print("tag was not found\n")

    else:
        if(paragraphOutput == None):
            print("tag was also not found")
        else:
            print(paragraphOutput)
        





