# Tai Sakuma <tai.sakuma@cern.ch>
from .determin_bintypeId import determin_bintypeId

##__________________________________________________________________||
class bintypeId(object):
    def begin(self, event):
        self.addr_bintypeId = [ ]
        event.bintypeId = self.addr_bintypeId

    def event(self, event):
        event.bintypeId = self.addr_bintypeId
        bintypeId = determin_bintypeId(event.nJet40[0], event.nJet100[0], event.ht40[0])
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
