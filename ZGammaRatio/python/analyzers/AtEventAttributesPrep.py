from PhysicsTools.HeppyCore.utils.deltar import deltaR
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event

import math

##__________________________________________________________________||
class AtEventAttributesPrep(Analyzer):
    def process(self, event):
        self.readCollections( event.input )

        event.isData = [not self.cfg_comp.isMC]

        event.componentName = [self.cfg_comp.name]
        # e.g., "HTMHT_Run2015D_PromptReco_25ns"

        event.nVert = [len(event.goodVertices)]

        event.nMuonsVeto = [len(event.selectedMuons)]
        event.nElectronsVeto = [len([e for e in event.selectedElectrons if e.electronID(self.cfg_ana.electron_veto_id)])]
        event.nElectronsLoose = [len(event.selectedElectrons)]
        event.nPhotonsVeto = [len(event.selectedPhotons)]
        event.nMuonsSelection = [len([e for e in event.selectedMuons if e.pt() >= 20 and abs(e.eta()) < 2.4 and e.muonID(self.cfg_ana.muon_selection_id)])]
        event.nElectronsSelection = [len([e for e in event.selectedElectrons if e.pt() >= 20 and abs(e.eta()) < 2.4 and e.electronID(self.cfg_ana.electron_selection_id)])]
        event.nPhotonsSelection = [len([e for e in event.selectedPhotons if e.pt() >= 165 and abs(e.eta()) < 1.45 and e.passPhotonID(self.cfg_ana.photon_selection_id) and e.passPhotonIso(self.cfg_ana.photon_selection_id,"rhoArea")])]

        event.nIsoTracksVeto = [len(event.selectedIsoTrack)]
        event.nIsoTracksNoMuVeto = [len(event.isoTrackNoMu)]
        event.nIsoTracksNoEleVeto = [len(event.isoTrackNoEle)]
        event.nIsoTracksNoMuEleVeto = [len(event.isoTrackNoMuEle)]

        # event.jet40failedId = [e for e in event.cleanJets if e.pt() >= 40 and not e.jetID(self.cfg_ana.jetID)] # FIXME: this is wrong and not straightforward to fix, but we don't use it...
        # event.nJet40failedId = [len(event.jet40failedId)]

        event.nJet40 = [len([e for e in event.cleanJets if e.pt() > 40])]
        event.nJet40JECUp = [len([e for e in event.cleanJetsJECUp if e.pt() > 40])]
        event.nJet40JECDown = [len([e for e in event.cleanJetsJECDown if e.pt() > 40])]

        event.nJet100 = [len([e for e in event.cleanJets if e.pt() > 100])]
        event.nJet100JECUp = [len([e for e in event.cleanJetsJECUp if e.pt() > 100])]
        event.nJet100JECDown = [len([e for e in event.cleanJetsJECDown if e.pt() > 100])]

        event.nBJet40 = [len([e for e in event.cleanJets if e.pt() > 40 and e.btagWP("CSVv2IVFM")])]
        event.nBJet40JECUp = [len([e for e in event.cleanJetsJECUp if e.pt() > 40 and e.btagWP("CSVv2IVFM")])]
        event.nBJet40JECDown = [len([e for e in event.cleanJetsJECDown if e.pt() > 40 and e.btagWP("CSVv2IVFM")])]

        event.ht40 = [event.htJet40j] # the same as [sum([e.pt() for e in event.cleanJets if e.pt() > 40])]
        event.ht40JECUp = [sum([e.pt() for e in event.cleanJetsJECUp if e.pt() > 40])]
        event.ht40JECDown = [sum([e.pt() for e in event.cleanJetsJECDown if e.pt() > 40])]

        event.mht40_pt = [event.mhtJet40j] # the same as [math.sqrt(math.pow(sum([j.px() for j in event.cleanJets if j.pt() > 40]), 2) + math.pow(sum([j.py() for j in event.cleanJets if j.pt() > 40]), 2))]
        event.mht40JECUp_pt = [math.sqrt(math.pow(sum([j.px() for j in event.cleanJetsJECUp if j.pt() > 40]), 2) + math.pow(sum([j.py() for j in event.cleanJetsJECUp if j.pt() > 40]), 2))]
        event.mht40JECDown_pt = [math.sqrt(math.pow(sum([j.px() for j in event.cleanJetsJECDown if j.pt() > 40]), 2) + math.pow(sum([j.py() for j in event.cleanJetsJECDown if j.pt() > 40]), 2))]

        event.nJet40Fwd = [len([e for e in event.cleanJetsFwd if e.pt() > 40])]
        event.nJet40FwdJECUp = [len([e for e in event.cleanJetsFwdJECUp if e.pt() > 40])]
        event.nJet40FwdJECDown = [len([e for e in event.cleanJetsFwdJECDown if e.pt() > 40])]

        event.mtw = [event.mtw]
        event.mll = [event.mll]

        event.met_pt = [event.met.pt()]
        event.met_phi = [event.met.phi()]
        event.metNoEle_pt = [event.metNoEle.pt()]
        event.metNoEle_phi = [event.metNoEle.phi()]
        event.metNoMu_pt = [event.metNoMu.pt()]
        event.metNoMu_phi = [event.metNoMu.phi()]
        event.metNoPhoton_pt = [event.metNoPhoton.pt()]
        event.metNoPhoton_phi = [event.metNoPhoton.phi()]
        # event.metNoMuEle_pt = [event.metNoMuEle.pt()]
        # event.metNoMuEle_phi = [event.metNoMuEle.phi()]

        event.minDelRJetMu = [min([deltaR(j, x) for j in event.cleanJets for x in event.selectedMuons if j.pt() > 40] + [999])]
        event.minDelRJetMuJECUp = [min([deltaR(j, x) for j in event.cleanJetsJECUp for x in event.selectedMuons if j.pt() > 40] + [999])]
        event.minDelRJetMuJECDown = [min([deltaR(j, x) for j in event.cleanJetsJECDown for x in event.selectedMuons if j.pt() > 40] + [999])]
        event.minDelRJetEle = [min([deltaR(j, x) for j in event.cleanJets for x in event.selectedElectrons if j.pt() > 40] + [999])]
        event.minDelRJetEleJECUp = [min([deltaR(j, x) for j in event.cleanJetsJECUp for x in event.selectedElectrons if j.pt() > 40] + [999])]
        event.minDelRJetEleJECDown = [min([deltaR(j, x) for j in event.cleanJetsJECDown for x in event.selectedElectrons if j.pt() > 40] + [999])]
        event.minDelRJetPhoton = [min([deltaR(j, x) for j in event.cleanJets for x in event.selectedPhotons if j.pt() > 40] + [999])]
        event.minDelRJetPhotonJECUp = [min([deltaR(j, x) for j in event.cleanJetsJECUp for x in event.selectedPhotons if j.pt() > 40] + [999])]
        event.minDelRJetPhotonJECDown = [min([deltaR(j, x) for j in event.cleanJetsJECDown for x in event.selectedPhotons if j.pt() > 40] + [999])]

        event.jet_pt = [e.pt() for e in event.cleanJets]
        event.jet_phi = [e.phi() for e in event.cleanJets]
        event.jet_eta = [e.eta() for e in event.cleanJets]
        event.jet_chHEF = [e.chargedHadronEnergyFraction() for e in event.cleanJets]

        event.jetJECUp_pt = [e.pt() for e in event.cleanJetsJECUp]
        event.jetJECUp_phi = [e.phi() for e in event.cleanJetsJECUp]

        event.jetJECDown_pt = [e.pt() for e in event.cleanJetsJECDown]
        event.jetJECDown_phi = [e.phi() for e in event.cleanJetsJECDown]

        event.Flag_HBHENoiseFilter = [event.Flag_HBHENoiseFilter]
        event.Flag_HBHENoiseIsoFilter = [event.Flag_HBHENoiseIsoFilter]
        event.Flag_EcalDeadCellTriggerPrimitiveFilter = [event.Flag_EcalDeadCellTriggerPrimitiveFilter]
        event.Flag_goodVertices = [event.Flag_goodVertices]
        event.Flag_eeBadScFilter = [event.Flag_eeBadScFilter]
        event.Flag_globalTightHalo2016Filter = [event.Flag_globalTightHalo2016Filter]

        if self.cfg_comp.isMC:
            event.lheHTnoT = [event.lheHTnoT]
            event.nLheElectrons = [event.nLheElectrons]
            event.nLheMuons = [event.nLheMuons]
            event.nLheTaus = [event.nLheTaus]

        if self.cfg_ana.metnohf:
            event.metNoHF_pt = [event.metNoHF.pt()]
            event.metNoHF_phi = [event.metNoHF.phi()]
            event.metNoEleNoHF_pt = [event.metNoEleNoHF.pt()]
            event.metNoEleNoHF_phi = [event.metNoEleNoHF.phi()]
            event.metNoMuNoHF_pt = [event.metNoMuNoHF.pt()]
            event.metNoMuNoHF_phi = [event.metNoMuNoHF.phi()]
            event.metNoPhotonNoHF_pt = [event.metNoPhotonNoHF.pt()]
            event.metNoPhotonNoHF_phi = [event.metNoPhotonNoHF.phi()]
            event.metNoMuEleNoHF_pt = [event.metNoMuEleNoHF.pt()]
            event.metNoMuEleNoHF_phi = [event.metNoMuEleNoHF.phi()]

            event.mtwNoHF = [event.mtwNoHF]

##__________________________________________________________________||
