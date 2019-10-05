# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class nPhotons200(object):
    def begin(self, event):
        self.vals = [ ]
        event.nPhotons200 = self.vals

    def event(self, event):
        event.nPhotons200 = self.vals
        self.vals[:] = [len([pt for pt in event.gamma_pt if pt >= 200])]

##__________________________________________________________________||
