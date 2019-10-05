from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.utils.deltar import deltaR2
import math
import ROOT
import os

##__________________________________________________________________||
class NIsrAnalyzer(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(NIsrAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.hOutW    = ROOT.TH1D("h_nIsr_weighted","N_{ISR} (weighted)",20,0.,20.)
        self.hOutW_up = ROOT.TH1D("h_nIsr_weighted_up","N_{ISR} (weighted up)",20,0.,20.)
        self.hOutW_down = ROOT.TH1D("h_nIsr_weighted_down","N_{ISR} (weighted down)",20,0.,20.)
        self.hOut     = ROOT.TH1D("h_nIsr_unweighted","N_{ISR} (unweighted)",20,0.,20.)

        # ISR weights
        self.weights = {}
        self.weights[0] = (1.,0.)
        self.weights[1] = (0.920,0.040)
        self.weights[2] = (0.821,0.090)
        self.weights[3] = (0.715,0.143)
        self.weights[4] = (0.662,0.169)
        self.weights[5] = (0.561,0.219)
        self.weights[6] = (0.511,0.244)

    def getNIsr(self, event):

        nIsr = 0

        for jet in event.cleanJetsAll:

            if jet.pt()<30.0: continue
            if abs(jet.eta())>2.4: continue
            matched = False
            for mc in event.genParticles:
                if matched: break
                if (mc.status()!=23 or abs(mc.pdgId())>5): continue
                momid = abs(mc.mother().pdgId())
                if not (momid==6 or momid==23 or momid==24 or momid==25 or momid>1e6): continue
                    #check against daughter in case of hard initial splitting
                for idau in range(mc.numberOfDaughters()):
                    dR = math.sqrt(deltaR2(jet.eta(),jet.phi(), mc.daughter(idau).p4().eta(),mc.daughter(idau).p4().phi()))
                    if dR<0.3:
                        matched = True
                        break
            if not matched:
                nIsr+=1

        return nIsr
        
        

    def process(self, event):

        #Can only be performed on MC
        if not self.cfg_comp.isMC: return True

        nIsr = self.getNIsr(event)
        event.nIsr = nIsr

        # Get the weight
        if nIsr <= 6: w,wErr = self.weights[nIsr][0],self.weights[nIsr][1] 
        else: w,wErr = self.weights[6][0],self.weights[6][1]

        # Fill the histograms
        self.hOut.Fill(nIsr)
        self.hOutW.Fill(nIsr,w)
        self.hOutW_up.Fill(nIsr,w+wErr)
        self.hOutW_down.Fill(nIsr,w-wErr)

        pass

        return True


    def write(self, setup):
        super(NIsrAnalyzer,self).write(setup)
        filePath = os.path.join(self.dirName, 'nIsrHistos.root')
        file = ROOT.TFile(filePath, 'recreate', "", 9)
        if self.hOut != None: self.hOut.Write()
        if self.hOutW != None: self.hOutW.Write()
        if self.hOutW_up != None: self.hOutW_up.Write()
        if self.hOutW_down != None: self.hOutW_down.Write()
        file.Close()

 

##__________________________________________________________________||
