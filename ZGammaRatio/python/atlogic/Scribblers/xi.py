# Tai Sakuma <tai.sakuma@cern.ch>
import numpy as np

##__________________________________________________________________||
class xi(object):
    def __init__(self, srcMinDphiTilde = 'minDphiTilde', srcMaxH = 'maxH', outName = 'xi',
                 default_empty = False, default_value = -1
    ):
        self.srcMinDphiTilde = srcMinDphiTilde
        self.srcMaxH = srcMaxH
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

        sinMinDphiTilde = np.sin(getattr(event, self.srcMinDphiTilde))
        maxH = np.array(getattr(event, self.srcMaxH))

        if not (sinMinDphiTilde.size == 1 and maxH.size == 1):
            if self.default_empty:
                self.out[:] = [ ]
            else:
                self.out[:] = [self.default_value]
            return

        self.out[:] = np.arctan2(sinMinDphiTilde, maxH)

##__________________________________________________________________||
