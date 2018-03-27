from bs4 import BeautifulSoup
import urllib2
import re
from sets import Set
from src.myFilters.factoryFilter import getFilter



def getPageFromLink(link,newsPapersName):
    print 'Get page from link:'+link
    links = Set()
    html_page = urllib2.urlopen(link)
    soup = BeautifulSoup(html_page)
    filter = getFilter(newsPapersName)
    print 'I have the filter'
    if filter is None:
        print 'Filter is None'
        return False
    try:
        for link in soup.findAll('a', attrs={'href': re.compile('^/')}):
            if filter.isARelativeLink(link):
                links.add(link.get('href'))
        for link in links:
            print link
        print 'Ok'
        return True
    except:
        print 'Some error when try get a page'
        return False
