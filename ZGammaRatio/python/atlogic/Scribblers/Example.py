# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class Example(object):
    def begin(self, event):
        self.vals = [ ]
        self.val = 0
        event.val = self.vals

    def event(self, event):
        event.val = self.vals
        self.val += 1
        self.vals[:] = [self.val]

##__________________________________________________________________||
