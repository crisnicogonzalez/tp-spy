from ClarinFilter import ClarinFilter

clarin = ClarinFilter()


def getFilter(newsPapers):
    {
    'Clarin':clarin
    }[newsPapers]
