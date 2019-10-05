# Tai Sakuma <tai.sakuma@cern.ch>
from .determin_bintypeId import determin_bintypeId

##__________________________________________________________________||
class bintypeIdJECDown(object):
    def begin(self, event):
        self.addr_bintypeId = [ ]
        event.bintypeIdJECDown = self.addr_bintypeId

    def event(self, event):
        event.bintypeIdJECDown = self.addr_bintypeId
        bintypeId = determin_bintypeId(event.nJet40JECDown[0], event.nJet100JECDown[0], event.ht40JECDown[0])
        self.addr_bintypeId[:] = [bintypeId]

##__________________________________________________________________||
