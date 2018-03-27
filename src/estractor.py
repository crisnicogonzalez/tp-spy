import requests
from bs4 import BeautifulSoup
import urllib2
import re
from sets import Set
from FactorFilter import getFilter




def getPageFromLink(link,newsPapersName):
    print 'Get page from link:'+link
    try:
        links = Set()
        html_page = urllib2.urlopen(link)
        soup = BeautifulSoup(html_page)
        filter = getFilter(newsPapersName)
        for link in soup.findAll('a', attrs={'href': re.compile('^/')}):
            if(filter.isARelativeLink(link)):
                links.add(link.get('href'))
        for link in links:
            print link
        return True
    except:
        return False
