from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

# try:
#     html = urlopen('http://pythonscraping.com/pages/page1.html')
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print("the server could not be found\n ")
# else:
#     print("The server successfully found\n")
#     bs = BeautifulSoup(html.read(),'lxml')

#     try:
#         paragraphOutput = bs.body.div
#     except AttributeError as e:
#         print("tag was not found\n")

#     else:
#         if(paragraphOutput == None):
#             print("tag was also not found")
#         else:
#             print(paragraphOutput)
       
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        print("bad url!")
    try:
        bs = BeautifulSoup(html.read(), 'lxml')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("https://www.pythoscraping.com/pages/page1.html")
if (title == None):
    print("The title could not be found\n")
else:
    print(title)




