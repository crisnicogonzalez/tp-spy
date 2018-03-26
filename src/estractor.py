import requests


def getPageFromLink(link):
    print 'Get page from link:'+link
    try:
        response = requests.get(link)
        print response.status_code
        print response.text
        return True
    except Error:
        return False
