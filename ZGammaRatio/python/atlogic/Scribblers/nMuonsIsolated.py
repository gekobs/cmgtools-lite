# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class nMuonsIsolated(object):
    def begin(self, event):
        self.vals = [ ]
        event.nMuonsIsolated = self.vals

    def event(self, event):
        event.nMuonsIsolated = self.vals
        self.vals[:] = [len([v for v in event.muon_relIso04 if v < 0.12])]

##__________________________________________________________________||
