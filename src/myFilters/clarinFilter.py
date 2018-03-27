from src.myFilters.abstractFilter import AbstractFilter

class ClarinFilter(AbstractFilter):
    def __init__(self):
        self.name = 'Clarin'

    def isARelativeLink(self, link):
        print 'ClarinFilter isARelativeLink'
        return link.find('//') < 0
