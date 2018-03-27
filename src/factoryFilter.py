from clarinFilter import ClarinFilter
from laNacionFilter import LaNacionFilter


clarin = ClarinFilter()
laNacion = LaNacionFilter()

def getFilter(newsPaperName):
    print 'get filter of:'+newsPaperName
    adict = {
    'Clarin':clarin,
    'La Nacion':laNacion
    }
    adict[newsPaperName]
