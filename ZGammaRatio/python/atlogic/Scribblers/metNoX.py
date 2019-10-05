# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class metNoX(object):
    def begin(self, event):
        self.val_pt = [ ]
        self.val_phi = [ ]
        event.metNoX_pt = self.val_pt
        event.metNoX_phi = self.val_phi
        self.itsdict = {
            1: ('met_pt', 'met_phi'), # 'Signal'
            2: ('metNoMu_pt', 'metNoMu_phi'), # 'SingleMu'
            3: ('metNoMu_pt', 'metNoMu_phi'), # 'DoubleMu'
            4: ('metNoEle_pt', 'metNoEle_phi'), # 'SingleEle'
            5: ('metNoEle_pt', 'metNoEle_phi'), # 'DoubleEle'
            6: ('metNoPhoton_pt', 'metNoPhoton_phi'), # 'SinglePhoton'
            # 7: ('metNoMuEle_pt', 'metNoMuEle_phi'), # 'SingleMuEle'
        }

    def event(self, event):
        event.metNoX_pt = self.val_pt
        event.metNoX_phi = self.val_phi
        cutflowId = event.cutflowId[0]
        if not cutflowId in self.itsdict: cutflowId = 1 # 'Signal'
        self.val_pt[:] = [getattr(event, self.itsdict[cutflowId][0])[0]]
        self.val_phi[:] = [getattr(event, self.itsdict[cutflowId][1])[0]]

##__________________________________________________________________||
