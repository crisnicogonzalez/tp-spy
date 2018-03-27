from clarinFilter import ClarinFilter
from laNacionFilter import LaNacionFilter


clarin = ClarinFilter()
laNacion = LaNacionFilter()

def getFilter(newsPaperName):
    return {
    'Clarin':clarin,
    'La Nacion':laNacion
    }[newsPaperName]
