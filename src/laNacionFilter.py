from abstractFilter import AbstractFilter

class LaNacionFilter(AbstractFilter):
    def __init__(self):
        self.name = 'La Nacion'
    def isARelativeLink(self,link):
        print 'LaNacionFilter isARelativeLink'
        return link.find('//') < 0
