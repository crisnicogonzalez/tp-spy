from abstractFilter import AbstractFilter

class ClarinFilter(AbstractFilter):
    def isARelativeLink(self,link):
        print 'ClarinFilter isARelativeLink'
        return link.find('//') < 0
