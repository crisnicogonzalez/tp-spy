from bs4 import BeautifulSoup
import urllib2
import re
from sets import Set
from factoryFilter import getFilter



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
    for link in soup.findAll('a', attrs={'href': re.compile('^/')}):
        print 'link -> '+link.get('href')
        if(filter.isARelativeLink(link)):
            links.add(link.get('href'))
    for link in links:
        print link
    print 'Ok'
    print 'Some error when try get a page'
    return True
