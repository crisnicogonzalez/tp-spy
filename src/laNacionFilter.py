from abstractFilter import AbstractFilter

class LaNacionFilter(AbstractFilter):
    def isARelativeLink(self,link):
        print 'LaNacionFilter isARelativeLink'
        return link.find('//') < 0
