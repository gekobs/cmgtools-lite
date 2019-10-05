# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class tan(object):
    def __init__(self, srcName, outName):
        self.srcName = srcName
        self.outName = outName

    def begin(self, event):
        self.out = [ ]
        self._attach_to_event(event)

    def _attach_to_event(self, event):
        setattr(event, self.outName, self.out)

    def event(self, event):
        self._attach_to_event(event)

        src = np.array(getattr(event, self.srcName))
        out = np.tan(src)
        self.out[:] = out


##__________________________________________________________________||
