from AbstractFilter import AbstractFilter



class ClarinFilter(AbstractFilter):
    def isARelativeLink(self,link):
        return link.find('//') < 0
