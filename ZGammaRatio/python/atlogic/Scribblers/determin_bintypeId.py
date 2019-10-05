# Tai Sakuma <tai.sakuma@cern.ch>
from ..Binning import Binning

##__________________________________________________________________||
class Determin_bintypeId(object):
    def __init__(self):
        self.njet40binning = Binning(boundaries = (1, 2))
        self.njet100binning = Binning(boundaries = (1, 2))
        self.htbinning = Binning(boundaries = (200, 800))

        # (nJet40, nJet100, ht40)
        self.tuple_bintypeId_dict = {
            (1, 1, 200) : 1, # 'monojet',
            (2, 1, 200) : 2, # 'asymjet',
            (2, 2, 200) : 3, # 'symjet',
            (1, 1, 800) : 1, # 'monojet',
            (2, 1, 800) : 4, # 'highht',
            (2, 2, 800) : 4, # 'highht',
        }

    def __call__(self, nJet40, nJet100, ht40):
        key = (self.njet40binning(nJet40), self.njet100binning(nJet100), self.htbinning(ht40))
        if key in self.tuple_bintypeId_dict:
            bintypeId = self.tuple_bintypeId_dict[key]
        else:
            bintypeId = -1
        return bintypeId

determin_bintypeId = Determin_bintypeId()

##__________________________________________________________________||
bintype_name_dict = {
    1 : 'monojet', 2 : 'asymjet', 3 : 'symjet', 4 : 'highht',
    -1 : 'other'
}

##__________________________________________________________________||
