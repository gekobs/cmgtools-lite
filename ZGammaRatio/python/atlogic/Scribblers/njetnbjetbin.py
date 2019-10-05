# Tai Sakuma <tai.sakuma@cern.ch>
from ..Binning import Binning

##__________________________________________________________________||
class njetnbjetbin(object):
    def __init__(self):
        self.nbjet40binning = Binning(boundaries = (0, 1, 2, 3))
        self.njet40binning = Binning(boundaries = (1, 2, 3, 4, 5))
        self.njet100binning = Binning(boundaries = (1, 2))

    def begin(self, event):
        self.vals = [ ]
        event.njetnbjetbin = self.vals

        # (nBJet40, nJet40, nJet100)
        self.bindict = {
            # monojet bins
            (0, 1, 1) : 'eq0b_eq1j', (1, 1, 1) : 'eq1b_eq1j',

            # asymetric bins
            (0, 2, 1) : 'eq0b_eq2a', (1, 2, 1) : 'eq1b_eq2a', (2, 2, 1) : 'eq2b_eq2a',
            (0, 3, 1) : 'eq0b_eq3a', (1, 3, 1) : 'eq1b_eq3a', (2, 3, 1) : 'eq2b_eq3a', (3, 3, 1) : 'ge3b_eq3a',
            (0, 4, 1) : 'eq0b_eq4a', (1, 4, 1) : 'eq1b_eq4a', (2, 4, 1) : 'eq2b_eq4a', (3, 4, 1) : 'ge3b_eq4a',
            (0, 5, 1) : 'eq0b_ge5a', (1, 5, 1) : 'eq1b_ge5a', (2, 5, 1) : 'eq2b_ge5a', (3, 5, 1) : 'ge3b_ge5a',

            # symetric bins
            (0, 2, 2) : 'eq0b_eq2j', (1, 2, 2) : 'eq1b_eq2j', (2, 2, 2) : 'eq2b_eq2j',
            (0, 3, 2) : 'eq0b_eq3j', (1, 3, 2) : 'eq1b_eq3j', (2, 3, 2) : 'eq2b_eq3j', (3, 3, 2) : 'ge3b_eq3j',
            (0, 4, 2) : 'eq0b_eq4j', (1, 4, 2) : 'eq1b_eq4j', (2, 4, 2) : 'eq2b_eq4j', (3, 4, 2) : 'ge3b_eq4j',
            (0, 5, 2) : 'eq0b_ge5j', (1, 5, 2) : 'eq1b_ge5j', (2, 5, 2) : 'eq2b_ge5j', (3, 5, 2) : 'ge3b_ge5j',
            }

    def event(self, event):
        event.njetnbjetbin = self.vals
        key = (
            self.nbjet40binning(event.nBJet40[0]),
            self.njet40binning(event.nJet40[0]),
            self.njet100binning(event.nJet100[0])
        )
        if key not in self.bindict:
            self.vals[:] = ['other']
            return
        self.vals[:] = [self.bindict[key]]

##__________________________________________________________________||
