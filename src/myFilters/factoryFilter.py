from src.myFilters.clarinFilter import ClarinFilter
from src.myFilters.laNacionFilter import LaNacionFilter


clarin = ClarinFilter()
laNacion = LaNacionFilter()

def getFilter(newsPaperName):
    return {
    'Clarin':clarin,
    'La Nacion':laNacion
    }[newsPaperName]
