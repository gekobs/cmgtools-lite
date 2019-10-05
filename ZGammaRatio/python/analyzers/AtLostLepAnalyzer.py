from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
import PhysicsTools.HeppyCore.framework.config as cfg

from PhysicsTools.Heppy.physicsutils.genutils import realGenMothers

import ROOT
from array import array

class AtLostLepAnalyzer( Analyzer ):
    """This computes the necessary quantities for the lost lepton background"""
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(AtLostLepAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)

    def beginLoop(self,setup):
        super(AtLostLepAnalyzer,self).beginLoop(setup)

        nJetBins = [0,1,2,3,4,5,6,99]
        nBJetBins = [0,1,2,3,4,99]
        htBins = [200., 250., 300., 350., 400., 500., 600., 750., 900., 1050., 1200., 9999.]
        self.outFile = ROOT.TFile(self.dirName+"/lep.root","recreate")
        self.outFile.cd()
        self.hists = {}
        
        # lepton with veto WP hist
        self.hists["muonAccepTop"] = ROOT.TH3D("muonAccTop","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["allMuonTop"] = ROOT.TH3D("allMuonTop","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["muonAccepW"] = ROOT.TH3D("muonAccW","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["allMuonW"] = ROOT.TH3D("allMuonW","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["eleAccepTop"] = ROOT.TH3D("eleAccTop","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["allEleTop"] = ROOT.TH3D("allEleTop","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["eleAccepW"] = ROOT.TH3D("eleAccW","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["allEleW"] = ROOT.TH3D("allEleW","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))

        for idx in range(1,self.cfg_ana.nIndex+1):
            self.hists["lheWeightHist_%s_allEleTop"%idx] = ROOT.TH1D("lheWeightHist_%s_allEleTop"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_AccepEleTop"%idx] = ROOT.TH1D("lheWeightHist_%s_AccepEleTop"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_allMuonTop"%idx] = ROOT.TH1D("lheWeightHist_%s_allMuonTop"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_AccepMuonTop"%idx] = ROOT.TH1D("lheWeightHist_%s_AccepMuonTop"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_allEleW"%idx] = ROOT.TH1D("lheWeightHist_%s_allEleW"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_AccepEleW"%idx] = ROOT.TH1D("lheWeightHist_%s_AccepEleW"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_allMuonW"%idx] = ROOT.TH1D("lheWeightHist_%s_allMuonW"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_AccepMuonW"%idx] = ROOT.TH1D("lheWeightHist_%s_AccepMuonW"%idx,"",200,0.,5000.)

        # lepton with selection WP hist
        self.hists["muonSelAccepTop"] = ROOT.TH3D("muonSelAccTop","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["allMuonSelTop"] = ROOT.TH3D("allMuonSelTop","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["muonSelAccepW"] = ROOT.TH3D("muonSelAccW","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["allMuonSelW"] = ROOT.TH3D("allMuonSelW","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["eleSelAccepTop"] = ROOT.TH3D("eleSelAccTop","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["allEleSelTop"] = ROOT.TH3D("allEleSelTop","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["eleSelAccepW"] = ROOT.TH3D("eleSelAccW","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))
        self.hists["allEleSelW"] = ROOT.TH3D("allEleSelW","",len(nJetBins)-1,array('d',nJetBins),len(nBJetBins)-1,array('d',nBJetBins),len(htBins)-1,array('d',htBins))

        for idx in range(1,self.cfg_ana.nIndex+1):
            self.hists["lheWeightHist_%s_allEleSelTop"%idx] = ROOT.TH1D("lheWeightHist_%s_allEleSelTop"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_AccepEleSelTop"%idx] = ROOT.TH1D("lheWeightHist_%s_AccepEleSelTop"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_allMuonSelTop"%idx] = ROOT.TH1D("lheWeightHist_%s_allMuonSelTop"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_AccepMuonSelTop"%idx] = ROOT.TH1D("lheWeightHist_%s_AccepMuonSelTop"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_allEleSelW"%idx] = ROOT.TH1D("lheWeightHist_%s_allEleSelW"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_AccepEleSelW"%idx] = ROOT.TH1D("lheWeightHist_%s_AccepEleSelW"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_allMuonSelW"%idx] = ROOT.TH1D("lheWeightHist_%s_allMuonSelW"%idx,"",200,0.,5000.)
            self.hists["lheWeightHist_%s_AccepMuonSelW"%idx] = ROOT.TH1D("lheWeightHist_%s_AccepMuonSelW"%idx,"",200,0.,5000.)
      

    def process(self,event):

        nJet40 = len([e for e in event.cleanJets if e.pt() > 40])
        nBJet40 = len([e for e in event.cleanJets if e.pt() > 40 and e.btagWP("CSVv2IVFM")])
        ht40 = event.htJet40j

        event.genLepsFromTop,event.genLepsFromW = self.makeGenLeps(event)
        event.genLepsFromTop.sort(key=lambda l: l.pt(), reverse = True)
        event.genLepsFromW.sort(key=lambda l: l.pt(), reverse = True)

        event.lostLepsTop = [ genLep for genLep in event.genLepsFromTop if self.checkAccep(genLep) ]
        event.lostLepsW = [ genLep for genLep in event.genLepsFromW if self.checkAccep(genLep) ]

        for genLep in event.genLepsFromW:
            if (abs(genLep.pdgId()) == 11):
                self.hists["allEleW"].Fill( nJet40 , nBJet40 , ht40 )
                for idx in range(1,self.cfg_ana.nIndex+1):
                    self.hists["lheWeightHist_%s_allEleW"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt )
                if self.checkAccep(genLep):
                    self.hists["eleAccepW"].Fill( nJet40 , nBJet40 , ht40 )
                    for idx in range(1,self.cfg_ana.nIndex+1):
                        self.hists["lheWeightHist_%s_AccepEleW"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)
                if self.checkAccep(genLep,2.1,30.):
                    self.hists["eleSelAccepW"].Fill( nJet40 , nBJet40 , ht40 )
                    for idx in range(1,self.cfg_ana.nIndex+1):
                        self.hists["lheWeightHist_%s_AccepEleSelW"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)

            elif (abs(genLep.pdgId()) == 13):
                self.hists["allMuonW"].Fill( nJet40 , nBJet40 , ht40 )
                for idx in range(1,self.cfg_ana.nIndex+1):
                    self.hists["lheWeightHist_%s_allMuonW"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)
                if self.checkAccep(genLep):
                    self.hists["muonAccepW"].Fill( nJet40 , nBJet40 , ht40 )
                    for idx in range(1,self.cfg_ana.nIndex+1):
                        self.hists["lheWeightHist_%s_AccepMuonW"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)
                if self.checkAccep(genLep,2.1,30.):
                    self.hists["muonAccepSelW"].Fill( nJet40 , nBJet40 , ht40 )
                    for idx in range(1,self.cfg_ana.nIndex+1):
                        self.hists["lheWeightHist_%s_AccepMuonSelW"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)

        for genLep in event.genLepsFromTop:
            if (abs(genLep.pdgId()) == 11):
                self.hists["allEleTop"].Fill( nJet40 , nBJet40 , ht40 )
                for idx in range(1,self.cfg_ana.nIndex+1):
                    self.hists["lheWeightHist_%s_allEleTop"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)
                if self.checkAccep(genLep):
                    self.hists["eleAccepTop"].Fill( nJet40 , nBJet40 , ht40 )
                    for idx in range(1,self.cfg_ana.nIndex+1):
                        self.hists["lheWeightHist_%s_AccepEleTop"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)
                if self.checkAccep(genLep,2.1,30.):
                    self.hists["eleSelAccepTop"].Fill( nJet40 , nBJet40 , ht40 )
                    for idx in range(1,self.cfg_ana.nIndex+1):
                        self.hists["lheWeightHist_%s_AccepEleSelTop"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)

            elif (abs(genLep.pdgId()) == 13):
                self.hists["allMuonTop"].Fill( nJet40 , nBJet40 , ht40 )
                for idx in range(1,self.cfg_ana.nIndex+1):
                    self.hists["lheWeightHist_%s_allMuonTop"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)
                if self.checkAccep(genLep):
                    self.hists["muonAccepTop"].Fill( nJet40 , nBJet40 , ht40 )
                    for idx in range(1,self.cfg_ana.nIndex+1):
                        self.hists["lheWeightHist_%s_AccepMuonTop"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)
                if self.checkAccep(genLep,2.1,30.):
                    self.hists["muonSelAccepTop"].Fill( nJet40 , nBJet40 , ht40 )
                    for idx in range(1,self.cfg_ana.nIndex+1):
                        self.hists["lheWeightHist_%s_AccepMuonSelTop"%idx].Fill( event.lheV_pt , event.LHE_weights[idx].wgt)

        event.nGenLepFromTop = len(event.genLepsFromTop)
        event.nGenLepFromW = len(event.genLepsFromW)
        event.nLostLepTop = len(event.lostLepsTop)
        event.nLostLepW = len(event.lostLepsW)

        return True
    
    def write(self,setup):
        super(AtLostLepAnalyzer,self).write(setup)
        self.outFile.cd()
        for histName,hist in self.hists.iteritems():
            hist.Write()
        self.outFile.Close()

    def makeGenLeps(self,event):
        """return gen leps coming from W or top decay"""

        genLepsFromTop = []
        genLepsFromW = []
        
        for p in event.generatorSummary:
            id = abs(p.pdgId())
            # Check if it is muon or ele
            if id not in [11,13]: continue            

            momids = [(m, abs(m.pdgId())) for m in realGenMothers(p)]

            for mom, momid in momids:
                if momid == 24:
                    wmomids = [abs(m.pdgId()) for m in realGenMothers(mom)]
                    if 6 in wmomids:
                        genLepsFromTop.append ( p )
                    else:
                        genLepsFromW.append( p )

        return genLepsFromTop,genLepsFromW

    def checkAccep(self,genLep,etaMax=2.5,ptMin=10.):

        if abs(genLep.eta()) > etaMax:
            return False
        
        if abs(genLep.pt()) < ptMin:
            return True

        return True
