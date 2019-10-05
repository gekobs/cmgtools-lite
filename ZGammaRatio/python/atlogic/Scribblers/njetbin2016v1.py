# Tai Sakuma <tai.sakuma@cern.ch>
from ..Binning import Binning

##__________________________________________________________________||
class njetbin2016v1(object):
    def __init__(self):
        self.njet40binning = Binning(boundaries = (1, 2, 3, 4, 5, 6))
        self.njet100binning = Binning(boundaries = (1, 2))

    def begin(self, event):
        self.vals = [ ]
        event.njetbin2016v1 = self.vals

        # (nJet40, nJet100)
        self.bindict = {
            # monojet bins
            (1, 1) : 'eq1j',

            # asymetric bins
            (2, 1) : 'ge2a', (3, 1) : 'ge2a', (4, 1) : 'ge2a',
            (5, 1) : 'ge2a', (6, 1) : 'ge2a',

            # symetric bins
            (2, 2) : 'eq2j', (3, 2) : 'eq3j', (4, 2) : 'eq4j',
            (5, 2) : 'eq5j', (6, 2) : 'ge6j',
            }

    def event(self, event):
        event.njetnbjetbin = self.vals
        key = (
            self.njet40binning(event.nJet40[0]),
            self.njet100binning(event.nJet100[0])
        )
        if key not in self.bindict:
            self.vals[:] = ['other']
            return
        self.vals[:] = [self.bindict[key]]

##__________________________________________________________________||
