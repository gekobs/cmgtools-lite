# Tai Sakuma <tai.sakuma@cern.ch>
from .determin_bintypeId import determin_bintypeId

##__________________________________________________________________||
class bintypeIdJECUp(object):
    def begin(self, event):
        self.addr_bintypeId = [ ]
        event.bintypeIdJECUp = self.addr_bintypeId

    def event(self, event):
        event.bintypeIdJECUp = self.addr_bintypeId
        bintypeId = determin_bintypeId(event.nJet40JECUp[0], event.nJet100JECUp[0], event.ht40JECUp[0])
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
