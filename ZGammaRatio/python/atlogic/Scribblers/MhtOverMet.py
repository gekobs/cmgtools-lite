# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class MhtOverMet(object):
    def begin(self, event):
        self.vals = [ ]
        event.MhtOverMet = self.vals

    def event(self, event):
        event.MhtOverMet = self.vals
        if event.met_pt[0] <= 0.00:
            self.vals[:] = [float("inf")]
            return
        self.vals[:] = [event.mht40_pt[0]/event.met_pt[0]]

##__________________________________________________________________||
