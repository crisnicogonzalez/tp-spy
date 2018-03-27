from clarinFilter import ClarinFilter

clarin = ClarinFilter()


def getFilter(newsPapers):
    {
    'Clarin':clarin
    }[newsPapers]
