# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class cutflowId(object):
    def begin(self, event):
        self.addr_cutflowId = [ ]
        event.cutflowId = self.addr_cutflowId
        # (nMuoV, nEleV, nPhoV, nMuoS, nEleS, nPhoS)
        self.nObjs_cutflowId_dict = {
            (0, 0, 0, 0, 0, 0) : 1, # 'Signal'
            (1, 0, 0, 1, 0, 0) : 2, # 'SingleMu'
            (2, 0, 0, 2, 0, 0) : 3, # 'DoubleMu'
            (0, 1, 0, 0, 1, 0) : 4, # 'SingleEle'
            (0, 2, 0, 0, 2, 0) : 5, # 'DoubleEle'
            (0, 0, 1, 0, 0, 1) : 6, # 'SinglePhoton'
            (1, 1, 0, 1, 1, 0) : 7, # 'SingleMuEle'
            }

    def event(self, event):
        event.cutflowId = self.addr_cutflowId
        key = (event.nMuonsVeto[0],
               event.nElectronsVeto[0],
               event.nPhotonsVeto[0],
               event.nMuonsSelection[0],
               event.nElectronsSelection[0],
               event.nPhotonsSelection[0]
        )
        if key in self.nObjs_cutflowId_dict:
            cutflowId = self.nObjs_cutflowId_dict[key]
        else:
            cutflowId = -1
        self.addr_cutflowId[:] = [cutflowId]

##__________________________________________________________________||
