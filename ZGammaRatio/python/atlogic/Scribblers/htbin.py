# Tai Sakuma <tai.sakuma@cern.ch>
from ..Binning import Binning

##__________________________________________________________________||
class htbin(object):
    def __init__(self):
        self.htbinning = Binning(boundaries = (200, 250, 300, 350, 400, 600, 800))

    def begin(self, event):
        self.vals = [ ]
        event.htbin = self.vals

    def event(self, event):
        event.htbin = self.vals
        self.vals[:] = [self.htbinning(event.ht40[0])]

##__________________________________________________________________||
