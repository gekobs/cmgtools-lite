# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class metNoXNoHF(object):
    def begin(self, event):
        self.val_pt = [ ]
        self.val_phi = [ ]
        event.metNoXNoHF_pt = self.val_pt
        event.metNoXNoHF_phi = self.val_phi
        self.itsdict = {
            1: ('metNoHF_pt', 'metNoHF_phi'), # 'Signal'
            2: ('metNoMuNoHF_pt', 'metNoMuNoHF_phi'), # 'SingleMu'
            3: ('metNoMuNoHF_pt', 'metNoMuNoHF_phi'), # 'DoubleMu'
            4: ('metNoEleNoHF_pt', 'metNoEleNoHF_phi'), # 'SingleEle'
            5: ('metNoEleNoHF_pt', 'metNoEleNoHF_phi'), # 'DoubleEle'
            6: ('metNoPhotonNoHF_pt', 'metNoPhotonNoHF_phi'), # 'SinglePhoton'
            7: ('metNoMuEleNoHF_pt', 'metNoMuEleNoHF_phi'), # 'SingleMuEle'
        }

    def event(self, event):
        event.metNoXNoHF_pt = self.val_pt
        event.metNoXNoHF_phi = self.val_phi
        cutflowId = event.cutflowId[0]
        if not cutflowId in self.itsdict: cutflowId = 1 # 'Signal'
        self.val_pt[:] = [getattr(event, self.itsdict[cutflowId][0])[0]]
        self.val_phi[:] = [getattr(event, self.itsdict[cutflowId][1])[0]]

##__________________________________________________________________||
