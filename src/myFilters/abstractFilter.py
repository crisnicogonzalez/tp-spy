from abc import ABCMeta,abstractmethod


class AbstractFilter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def isARelativeLink(self,link): pass
