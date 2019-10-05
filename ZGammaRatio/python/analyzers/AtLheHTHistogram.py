from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer

import math
import os
import ROOT as r

##__________________________________________________________________||
class AtLheHTHistogram(Analyzer):
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(AtLheHTHistogram, self).__init__(cfg_ana, cfg_comp, looperName)

        self.h_lheHT    = r.TH1D('lheHT', 'h_lheHT', 120, 0.0, 3000.0)
        self.h_lheHTnoT = r.TH1D('lheHTnoT', 'h_lheHTnoT', 120, 0.0, 3000.0)

    def process(self, event):
        if not self.cfg_comp.isMC: return True

        lheHT    = getattr(event, self.cfg_ana.object)
        lheHTnoT = getattr(event, self.cfg_ana.secondobject)    
        
        self.h_lheHT.Fill(lheHT)
        self.h_lheHTnoT.Fill(lheHTnoT)

        return True

    def write(self, setup):
        super(AtLheHTHistogram, self).write(setup)
        pathtofile = os.path.join(self.dirName, 'lheHTs.root')
        file = r.TFile(pathtofile, 'recreate')
        self.h_lheHT.Write()
        self.h_lheHTnoT.Write()
        file.Write()

##__________________________________________________________________||
