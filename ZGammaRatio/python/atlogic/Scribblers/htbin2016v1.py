# Tai Sakuma <tai.sakuma@cern.ch>
from ..Binning import Binning

##__________________________________________________________________||
class htbin2016v1(object):
    def __init__(self):
        self.htbinning = Binning(boundaries = (200, 400, 600, 900, 1200))

    def begin(self, event):
        self.vals = [ ]
        event.htbin2016v1 = self.vals

    def event(self, event):
        event.htbin = self.vals
        self.vals[:] = [self.htbinning(event.ht40[0])]

##__________________________________________________________________||
