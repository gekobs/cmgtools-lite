# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class nElectronsIsolated(object):
    def begin(self, event):
        self.vals = [ ]
        event.nElectronsIsolated = self.vals

    def event(self, event):
        event.nElectronsIsolated = self.vals
        self.vals[:] = [len([(iso, eta) for iso, eta in zip(event.ele_relIso04, event.ele_eta) if self._isIsolated(iso, eta)])]

    def _isIsolated(self, iso, eta):
        if -1.479 < eta < 1.479:
            return iso < 0.0354
        else:
            return iso < 0.0646

##__________________________________________________________________||
