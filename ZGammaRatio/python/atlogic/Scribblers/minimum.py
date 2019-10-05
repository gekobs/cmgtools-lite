# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class minimum(object):
    def __init__(self, srcName, outName, default_empty = False, default_value = None):
        self.srcName = srcName
        self.outName = outName
        self.default_empty = default_empty
        self.default_value = default_value

    def begin(self, event):
        self.out = [ ]
        self._attach_to_event(event)

    def _attach_to_event(self, event):
        setattr(event, self.outName, self.out)

    def event(self, event):
        self._attach_to_event(event)

        src = np.array(getattr(event, self.srcName))

        if src.size > 0:
            self.out[:] = [src.min().item()]
        elif self.default_empty:
            self.out[:] = [ ]
        else:
            self.out[:] = [self.default_value]


##__________________________________________________________________||
