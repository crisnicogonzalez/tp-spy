import requests


def getPageFromLink(link):
    print 'Get page from link:'+link
    response = requests.get(link)
    print response.status_code
    print response.text
