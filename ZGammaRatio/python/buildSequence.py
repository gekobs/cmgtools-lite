import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.core.all import *
from PhysicsTools.Heppy.analyzers.objects.all import *
from PhysicsTools.Heppy.analyzers.gen.all import *
#from CMGTools.RootTools.RootTools import *
import sys

##____________________________________________________________________________||
## SkimAnalyzer
skimAna = cfg.Analyzer(
    SkimAnalyzerCount, name="skimAnalyzerCount",
    useLumiBlocks=False,
    )

##____________________________________________________________________________||
## JSONAnalyzer
jsonAna = cfg.Analyzer(
    JSONAnalyzer, name="jsonAnalyzer",
    )

##____________________________________________________________________________||
## TriggerBitFilter
triggerAna = cfg.Analyzer(
    TriggerBitFilter, name="triggerBitFilter",
    )

##____________________________________________________________________________||
## VertexAnalyzer
vertexAna = cfg.Analyzer(
    VertexAnalyzer, name="vertexAnalyzer",
    vertexWeight=None,
    fixedWeight=1,
    verbose=False,
    keepFailingEvents=True,
    )

##____________________________________________________________________________||
## AtnVertCounter
from CMGTools.ZGammaRatio.analyzers.AtnVertCounter import AtnVertCounter
atnVertCounter = cfg.Analyzer(
    AtnVertCounter, name="AtnVertCounter",
    )

##____________________________________________________________________________||
## PileUpAnalyzer
pileUpAna = cfg.Analyzer(
    PileUpAnalyzer , name="pileUpAnalyzer",
    true=True, # use number of true interactions for reweighting
    makeHists=False,
    )

##____________________________________________________________________________||
## LHEWeightAnalyzer
lheWeightAna = cfg.Analyzer(
    LHEWeightAnalyzer, name="lheWeightAnalyzer",
    useLumiInfo=False,
    makeLHEweights=True, # Turn off lhe weights (slows everything down)
    )

##____________________________________________________________________________||
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer
lheAna = cfg.Analyzer(
    LHEAnalyzer, name = 'LHEAnalyzer',
    )

##____________________________________________________________________________||
## GeneratorAnalyzer
genAna = cfg.Analyzer(
    GeneratorAnalyzer, name="generatorAnalyzer",
    # BSM particles that can appear with status <= 2 and should be kept
    stableBSMParticleIds=[ 1000022 ],
    # Particles of which we want to save the pre-FSR momentum (a la status 3).
    # Note that for quarks and gluons the post-FSR doesn't make sense,
    # so those should always be in the list
    savePreFSRParticleIds=[ 1,2,3,4,5, 11,12,13,14,15,16, 21,22 ],
    # Make also the list of all genParticles, for other analyzers to handle
    makeAllGenParticles=True,
    # Make also the splitted lists
    makeSplittedGenLists=True,
    allGenTaus=False,
    # Print out debug information
    verbose=False,
    )

##____________________________________________________________________________||
## GenHeavyFlavourAnalyzer
genHFAna = cfg.Analyzer(
    GenHeavyFlavourAnalyzer, name="genHeavyFlavourAnalyzer",
    status2Only=False,
    bquarkPtCut=15.0,
    )

##____________________________________________________________________________||
## PDFWeightsAnalyzer
# PDFWeights = []
PDFWeights = [("CT10",53), ("MSTW2008lo68cl",41), ("NNPDF21_100",101)]

pdfwAna = cfg.Analyzer(
    PDFWeightsAnalyzer, name="pdfWeightsAnalyzer",
    PDFWeights=[ pdf for pdf,num in PDFWeights ],
    doPDFVars = True,
    )

##____________________________________________________________________________||
## LeptonAnalyzer
mu_id_selection = "POG_ID_Tight"
mu_id_loose     = "POG_ID_Loose"

ele_id_selection = 'POG_Cuts_ID_SPRING16_25ns_v1_ConvVetoDxyDz_Tight'
ele_id_loose     = 'POG_Cuts_ID_SPRING16_25ns_v1_ConvVetoDxyDz_Loose'
ele_id_veto      = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Medium'
ele_id_medium    = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Medium'

lepAna = cfg.Analyzer(
    LeptonAnalyzer, name="leptonAnalyzer",
    # input collections
    muons='slimmedMuons',
    electrons='slimmedElectrons',
    rhoMuon='fixedGridRhoFastjetCentralNeutral',
    rhoElectron ='fixedGridRhoFastjetCentralNeutral',
    # energy scale corrections and ghost muon suppression (off by default)
    doMuonScaleCorrections=False,
    doElectronScaleCorrections=False, # "embedded" in 5.18 for regression
    doSegmentBasedMuonCleaning=False,
    # inclusive very loose muon selection
    inclusive_muon_id  = "POG_ID_Loose",
    inclusive_muon_pt  = 3,
    inclusive_muon_eta = 2.4,
    inclusive_muon_dxy = 0.5,
    inclusive_muon_dz  = 1.0,
    muon_dxydz_track = "innerTrack",
    # loose muon selection
    loose_muon_id     = mu_id_loose,
    loose_muon_pt     = 10.,
    loose_muon_eta    = 2.5,
    loose_muon_dxy    = 999.,
    loose_muon_dz     = 999.,
    loose_muon_relIso = 0.12,
    # inclusive very loose electron selection
    inclusive_electron_id  = "",
    inclusive_electron_pt  = 5,
    inclusive_electron_eta = 2.5,
    inclusive_electron_dxy = 0.5,
    inclusive_electron_dz  = 1.0,
    inclusive_electron_lostHits = 1.0,
    # loose electron selection
    veto_electron_id      = ele_id_veto,
    loose_electron_id     = ele_id_loose,
    loose_electron_pt     = 10.,
    loose_electron_eta    = 2.5,
    loose_electron_dxy    = 0.118,
    loose_electron_dz     = 0.822,
    loose_electron_relIso = 0.12,
    loose_electron_lostHits = 1.0,
    # muon isolation correction method (can be "rhoArea" or "deltaBeta")
    mu_isoCorr = "deltaBeta" ,
    mu_effectiveAreas = "Spring15_25ns_v1", #(can be 'Data2012' or 'Phys14_25ns_v1' or 'Spring15_25ns_v1')
    mu_tightId = mu_id_selection,
    # electron isolation correction method (can be "rhoArea" or "deltaBeta")
    ele_isoCorr = "rhoArea" ,
    ele_effectiveAreas = "Spring15_25ns_v1" , #(can be 'Data2012' or 'Phys14_25ns_v1' or 'Spring15_25ns_v1')
    ele_tightId = ele_id_selection,
    # Mini-isolation, with pT dependent cone: will fill in the miniRelIso, miniRelIsoCharged, miniRelIsoNeutral variables of the leptons (see https://indico.cern.ch/event/368826/ )
    doMiniIsolation = False, # off by default since it requires access to all PFCandidates
    packedCandidates = 'packedPFCandidates',
    miniIsolationPUCorr = 'rhoArea', # Allowed options: 'rhoArea' (EAs for 03 cone scaled by R^2), 'deltaBeta', 'raw' (uncorrected), 'weights' (delta beta weights; not validated)
    miniIsolationVetoLeptons = None, # use 'inclusive' to veto inclusive leptons and their footprint in all isolation cones
    doDirectionalIsolation = [], # calculate directional isolation with leptons (works only with doMiniIsolation, pass list of cone sizes)
    doFixedConeIsoWithMiniIsoVeto = False, # calculate fixed cone isolations with the same vetoes used for miniIso,
    # minimum deltaR between a loose electron and a loose muon (on overlaps, discard the electron)
    min_dr_electron_muon = 0.05,
    # do MC matching
    do_mc_match = True, # note: it will in any case try it only on MC, not on data
    do_mc_match_photons = "all",
    match_inclusiveLeptons = False, # match to all inclusive leptons
    )

##____________________________________________________________________________||
## ttHLepSkimmer
from CMGTools.TTHAnalysis.analyzers.ttHLepSkimmer import ttHLepSkimmer
ttHLepSkim = cfg.Analyzer(
    ttHLepSkimmer, name='ttHLepSkimmer',
    minLeptons = 0,
    maxLeptons = 999,
    #idCut  = "lepton.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the leptons
    requireSameSignPair = False,
    allowLepTauComb = False
    )

##____________________________________________________________________________||
## PhotonAnalyzer
pho_id_loose                       = "POG_SPRING16_25ns_Loose"
pho_id_selection                   = "POG_SPRING16_25ns_Tight"
pho_id_selection_fakeEnriched      = "POG_SPRING16_25ns_Tight_noChaHadIso_noSigmaIEtaIEta"

photonAna = cfg.Analyzer(
    PhotonAnalyzer, name='photonAnalyzer',
    photons='slimmedPhotons',
    doPhotonScaleCorrections=False,
    ptMin=25,
    etaMax=2.5,
    gammaID=pho_id_loose,
    rhoPhoton='fixedGridRhoFastjetAll',
    gamma_isoCorr='rhoArea',
    effectiveAreas="SPRING16",
    conversionSafe_eleVeto=False, #if True candidate photon will have a matched prompt electron
    do_mc_match=True,
    do_randomCone=True,
    checkGen=True,
    )

##____________________________________________________________________________||
## TauAnalyzer
tauAna = cfg.Analyzer(
    TauAnalyzer, name="tauAnalyzer",
    etaMax = 2.3,
    vetoLaptons = True,
    vetoLeptonsPOG = False,
    # inclusive very loose hadronic tau selection
    inclusive_ptMin = 18,
    inclusive_etaMax = 9999,
    inclusive_dxyMax = 1000.,
    inclusive_dzMax = 0.4,
    inclusive_vetoLeptons = False,
    inclusive_leptonVetoDR = 0.4,
    inclusive_decayModeID = "decayModeFindingNewDMs", # ignored if not set or ""
    inclusive_tauID = "decayModeFindingNewDMs",
    inclusive_vetoLeptonsPOG = False, # If True, the following two IDs are required
    inclusive_tauAntiMuonID = "",
    inclusive_tauAntiElectronID = "",
    # loose hadronic tau selection
    loose_ptMin = 18,
    loose_etaMax = 9999,
    loose_dxyMax = 1000.,
    loose_dzMax = 0.2,
    loose_vetoLeptons = True,
    loose_leptonVetoDR = 0.4,
    loose_decayModeID = "decayModeFindingNewDMs", # ignored if not set or ""
    loose_tauID = "byLooseCombinedIsolationDeltaBetaCorr3Hits",
    loose_vetoLeptonsPOG = False, # If True, the following two IDs are required
    loose_tauAntiMuonID = "againstMuonLoose3",
    loose_tauAntiElectronID = "againstElectronLooseMVA5",
    )

##____________________________________________________________________________||
## IsoTrackAnalyzer
isoTrackAna = cfg.Analyzer(
    IsoTrackAnalyzer, name='isoTrackAnalyzer',
    setOff=False,
    #####
    candidates='packedPFCandidates',
    candidatesTypes='std::vector<pat::PackedCandidate>',
    ptMin = 10, # for pion
    ptMinEMU = 10, # for EMU
    dzMax = 0.05,
    #####
    isoDR = 0.3,
    ptPartMin = 0,
    dzPartMax = 0.05,
    maxAbsIso = 8,
    #####
    doRelIsolation = True,
    MaxIsoSum = 0.1, ### unused if not rel iso
    MaxIsoSumEMU = 0.1, ### unused if not rel iso
    doSecondVeto = False,
    #####
    doPrune = False,
    do_mc_match = False, # note: it will in any case try it only on MC, not on data
    )

##____________________________________________________________________________||
## JetAnalyzer
jetAna = cfg.Analyzer(
    JetAnalyzer, name='jetAnalyzer',
    jetCol = 'slimmedJets',
    copyJetsByValue = False,      #Whether or not to copy the input jets or to work with references (should be 'True' if JetAnalyzer is run more than once)
    genJetCol = 'slimmedGenJets',
    rho = ('fixedGridRhoFastjetAll','',''),
    jetID = "POG_PFID_Loose",
    jetPt = 10.,
    jetEta = 5.,
    jetEtaCentral = 3.0,
    cleanJetsFromLeptons = True,
    jetLepDR = 0.4,
    jetLepArbitration = (lambda jet,lepton : lepton), # you can decide which to keep in case of overlaps; e.g. if the jet is b-tagged you might want to keep the jet
    cleanSelectedLeptons = True, #Whether to clean 'selectedLeptons' after disambiguation. Treat with care (= 'False') if running Jetanalyzer more than once
    minLepPt = 10,
    lepSelCut = lambda lep : True,
    relaxJetId = False,
    doPuId = True,
    recalibrateJets = True, #'MC', # True, False, 'MC', 'Data'
    applyL2L3Residual = True, # Switch to 'Data' when they will become available for Data
    recalibrationType = "AK4PFchs",
    mcGT = "Summer16_07Aug2017_V11_MC",
    dataGT = [
        (1,      "Summer16_07Aug2017BCD_V11_DATA"),
        (276831, "Summer16_07Aug2017EF_V11_DATA"),
        (278802, "Summer16_07Aug2017GH_V11_DATA"),
        ],
    jecPath = "${CMSSW_BASE}/src/CMGTools/RootTools/data/jec",
    shiftJEC = 0, # set to +1 or -1 to apply +/-1 sigma shift to the nominal jet energies
    addJECShifts = True, # if true, add  "corr", "corrJECUp", and "corrJECDown" for each jet (requires uncertainties to be available!)
    jetPtOrUpOrDnSelection = False, # if true, apply pt cut on the maximum among central, JECUp and JECDown values of corrected pt
    smearJets = False,
    shiftJER = 0, # set to +1 or -1 to get +/-1 sigma shifts
    cleanAllJets = True,
    alwaysCleanPhotons = True,
    cleanGenJetsFromPhoton = True,
    cleanJetsFromFirstPhoton = False,
    cleanJetsFromTaus = False,
    cleanJetsFromIsoTracks = False,
    doQG = False,
    do_mc_match = True,
    collectionPostFix = "",
    calculateSeparateCorrections = True, # should be True if recalibrateJets is True, otherwise L1s will be inconsistent
    calculateType1METCorrection  = True,
    type1METParams = { 'jetPtThreshold':15., 'skipEMfractionThreshold':0.9, 'skipMuons':True },
    storeLowPtJets = False,
    )

##____________________________________________________________________________||
## METAnalyzer
metAna = cfg.Analyzer(
    METAnalyzer, name="metAnalyzer",
    metCollection     = "slimmedMETs",
    noPUMetCollection = "slimmedMETs",
    copyMETsByValue = False,
    doTkMet = False,
    doPuppiMet = False,
    doMetNoPU = True,
    doMetNoMu = True,
    doMetNoEle = True,
    doMetNoPhoton = True,
    doMetNoMuEle = True,
    storePuppiExtra = False,
    recalibrate = 'type1',
    applyJetSmearing = False, # does nothing unless the jet smearing is turned on in the jet analyzer
    old74XMiniAODs = False, # set to True to get the correct Raw MET when running on old 74X MiniAODs
    jetAnalyzerPostFix = "",
    candidates='packedPFCandidates',
    candidatesTypes='std::vector<pat::PackedCandidate>',
    dzMax = 0.1,
    fallbackLabel = None,
    collectionPostFix = "",
    )

##____________________________________________________________________________||
## ttHCoreEventAnalyzer:
##     Core Event Analyzer (computes basic quantities like HT, dilepton masses)
from CMGTools.TTHAnalysis.analyzers.ttHCoreEventAnalyzer import ttHCoreEventAnalyzer
ttHCoreEventAna = cfg.Analyzer(
    ttHCoreEventAnalyzer, name='ttHCoreEventAnalyzer',
    maxLeps = 4, ## leptons to consider
    mhtForBiasedDPhi = "mhtJet40jvec",
    jetForBiasedDPhi = "cleanJets",
    jetPt = 40.,
    doLeptonMVASoft = False,
    )

##____________________________________________________________________________||
## TriggerFlagsAnalyzer
from CMGTools.ZGammaRatio.components.triggerContent.baseTriggers_2016 import *
#from CMGTools.ZGammaRatio.components.triggerContent.fullTriggers_2016 import *
selectedTriggerBits = {}
selectedTriggerBits.update(signalTriggerBits)
selectedTriggerBits.update(hadronicTriggerBits)
selectedTriggerBits.update(monojetTriggerBits)
selectedTriggerBits.update(muonTriggerBits)
selectedTriggerBits.update(electronTriggerBits)
selectedTriggerBits.update(photonTriggerBits)
selectedTriggerBits.update(photonAlternativeTriggerBits)
selectedTriggerBits.update(comissioningTriggerBits)

triggerFlagsAna = cfg.Analyzer(
    TriggerBitAnalyzer, name="TriggerFlags",
    processName = 'HLT',
    fallbackProcessName = 'HLT2',
    prescaleProcessName = 'PAT',
    prescaleFallbackProcessName = 'RECO',
    unrollbits = False,
    saveIsUnprescaled = False,
    checkL1prescale = False,
    triggerBits = selectedTriggerBits,
    )

##____________________________________________________________________________||
## EventFlagsAnalyzer
eventFlagsAna = cfg.Analyzer(
    TriggerBitAnalyzer, name="EventFlags",
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    outprefix   = 'Flag',
    triggerBits = {
        "HBHENoiseFilter" : [ "Flag_HBHENoiseFilter" ],
        "HBHENoiseIsoFilter" : [ "Flag_HBHENoiseIsoFilter" ],
        "globalTightHalo2016Filter" : [ "Flag_globalTightHalo2016Filter" ],
        "CSCTightHalo2015Filter" : [ "Flag_CSCTightHalo2015Filter" ],
        "CSCTightHaloFilter" : [ "Flag_CSCTightHaloFilter" ],
        "CSCTightHalo2016Filter" : [ "Flag_globalTightHalo2016Filter" ],
        "hcalLaserEventFilter" : [ "Flag_hcalLaserEventFilter" ],
        "EcalDeadCellTriggerPrimitiveFilter" : [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ],
        "goodVertices" : [ "Flag_goodVertices" ],
        "trackingFailureFilter" : [ "Flag_trackingFailureFilter" ],
        "eeBadScFilter" : [ "Flag_eeBadScFilter" ],
        "ecalLaserCorrFilter" : [ "Flag_ecalLaserCorrFilter" ],
        "trkPOGFilters" : [ "Flag_trkPOGFilters" ],
        "trkPOG_manystripclus53X" : [ "Flag_trkPOG_manystripclus53X" ],
        "trkPOG_toomanystripclus53X" : [ "Flag_trkPOG_toomanystripclus53X" ],
        "trkPOG_logErrorTooManyClusters" : [ "Flag_trkPOG_logErrorTooManyClusters" ],
        "METFilters" : [ "Flag_METFilters" ],
        }
    )

##____________________________________________________________________________||
## BadMuonAnalyzer
from CMGTools.TTHAnalysis.analyzers.badMuonAnalyzer import badMuonAnalyzer
badMuonAna = cfg.Analyzer(
   badMuonAnalyzer, name = 'badMuonAna',
   muons='slimmedMuons',
   packedCandidates = 'packedPFCandidates',
   )

##____________________________________________________________________________||
## BadCloneMuonAnalyzer - Moriond2017
from CMGTools.TTHAnalysis.analyzers.badMuonAnalyzerMoriond2017 import badMuonAnalyzerMoriond2017
badCloneMuonAnaMoriond2017 = cfg.Analyzer(
    badMuonAnalyzerMoriond2017, name = 'badCloneMuonMoriond2017',
    muons = 'slimmedMuons',
    vertices = 'offlineSlimmedPrimaryVertices',
    minMuPt = lepAna.loose_muon_pt,
    selectClones = True,
    postFix = '',
    )

##____________________________________________________________________________||
## BadMuonAnalyzer - Moriond2017
badMuonAnaMoriond2017 = cfg.Analyzer(
    badMuonAnalyzerMoriond2017, name = 'badMuonMoriond2017',
    muons = 'slimmedMuons',
    vertices = 'offlineSlimmedPrimaryVertices',
    minMuPt = lepAna.loose_muon_pt,
    selectClones = False,
    postFix = '',
    )

##____________________________________________________________________________||
## BadChargedHadronAnalyzer
from CMGTools.TTHAnalysis.analyzers.badChargedHadronAnalyzer import badChargedHadronAnalyzer
badChargedHadronAna = cfg.Analyzer(
    badChargedHadronAnalyzer, name = 'badChargedHadronAna',
    muons='slimmedMuons',
    packedCandidates = 'packedPFCandidates',
    )


##____________________________________________________________________________||
## Muons
## Choose medium point from https://indico.cern.ch/event/357213/contribution/2/material/slides/0.pdf
## other things in https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonId2015

##____________________________________________________________________________||
## Electrons
## Choose loose point from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2

##____________________________________________________________________________||
## Photons (used for the veto)

##____________________________________________________________________________||
## Taus
# https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV

##____________________________________________________________________________||
# Jets (for event variables do apply the jetID and not PUID yet)

##____________________________________________________________________________||
## Isolated Track
# those are the cuts for the nonEMu

##____________________________________________________________________________||
## Jets with JEC variations
from CMGTools.ZGammaRatio.analyzers.AtJetsJECVariations import AtJetsJECVariations
atJetsJECVariations = cfg.Analyzer(
    AtJetsJECVariations, name='AtJetsJECVariations',
    jets_in = 'cleanJets',
    jets_out_up = 'cleanJetsJECUp',
    jets_out_down = 'cleanJetsJECDown',
    )

atJetsFwdJECVariations = cfg.Analyzer(
    AtJetsJECVariations, name='AtJetsFwdJECVariations',
    jets_in = 'cleanJetsFwd',
    jets_out_up = 'cleanJetsFwdJECUp',
    jets_out_down = 'cleanJetsFwdJECDown',
    )

# atFatJetsJECVariations = cfg.Analyzer(
#     AtJetsJECVariations, name='AtFatJetsJECVariations',
#     jets_in = 'cleanJetsAK8',
#     jets_out_up = 'cleanJetsAK8JECUp',
#     jets_out_down = 'cleanJetsAK8JECDown',
#     )

##____________________________________________________________________________||
from CMGTools.ZGammaRatio.analyzers.AtObjNoX import AtObjNoX
isoTrackNoMu = cfg.Analyzer(
    AtObjNoX, name = 'isoTrackNoMu',
    objects = 'selectedIsoTrack',
    X = ['selectedMuons'],
    outName = 'isoTrackNoMu',
    deltaR = 0.02
    )

isoTrackNoEle = cfg.Analyzer(
    AtObjNoX, name = 'isoTrackNoEle',
    objects = 'selectedIsoTrack',
    X = ['selectedElectrons'],
    outName = 'isoTrackNoEle',
    deltaR = 0.02
    )

isoTrackNoMuEle = cfg.Analyzer(
    AtObjNoX, name = 'isoTrackNoMuEle',
    objects = 'selectedIsoTrack',
    X = ['selectedMuons','selectedElectrons'],
    outName = 'isoTrackNoMuEle',
    deltaR = 0.02
    )

##____________________________________________________________________________||
from CMGTools.ZGammaRatio.analyzers.AtLheHTnoT import AtLheHTnoT
atLheHTnoT = cfg.Analyzer(
    AtLheHTnoT, name = 'AtLheHTnoT'
    )

##____________________________________________________________________________||
from CMGTools.ZGammaRatio.analyzers.AtLheN import AtLheN
atLheN = cfg.Analyzer(
    AtLheN, name = 'AtLheN',
    )

from CMGTools.ZGammaRatio.analyzers.AtLheHTHistogram import AtLheHTHistogram
atLheHTHistogram = cfg.Analyzer(
    AtLheHTHistogram, name = 'AtLheHTHistogram',
    object = 'lheHT',
    secondobject = 'lheHTnoT',
    )

##____________________________________________________________________________||
from CMGTools.ZGammaRatio.analyzers.AtMiscVarsCalculator import AtMiscVarsCalculator
atMiscVarsCalculator = cfg.Analyzer(
    AtMiscVarsCalculator, name='ttHAlphaTControlAnalyzer',
    doMetNoHF = False,
    )

##____________________________________________________________________________||
# Gen Info Analyzer
from CMGTools.TTHAnalysis.analyzers.ttHGenBinningAnalyzer import ttHGenBinningAnalyzer
ttHGenBinAna = cfg.Analyzer(
    ttHGenBinningAnalyzer, name = 'ttHGenBinningAnalyzer'
    )

##____________________________________________________________________________||
from CMGTools.TTHAnalysis.analyzers.hbheAnalyzer import hbheAnalyzer
HbheAnalyzer = cfg.Analyzer(
    hbheAnalyzer, name='hbheAnalyzer',
    bunchSp = '25ns',
    IgnoreTS4TS5ifJetInLowBVRegion = False,
    )

##____________________________________________________________________________||
# AtFatJetAna = cfg.Analyzer(
#     JetAnalyzer, name = 'AtFatJetAnalyzer',
#     jetCol = 'slimmedJetsAK8',
#     subjetCol = "SoftDrop",
#     copyJetsByValue = False,      #Whether or not to copy the input jets or to work with references (should be 'True' if JetAnalyzer is run more than once)
#     genJetCol = 'slimmedGenJets',
#     rho = ('fixedGridRhoFastjetAll','',''),
#     jetID = 'POG_PFID_Loose',
#     jetPt = 100.,
#     jetEta = 5.0,
#     jetEtaCentral = 3.,
#     jetLepDR = 0.4,
#     jetLepArbitration = (lambda jet,lepton : lepton), # you can decide which to keep in case of overlaps; e.g. if the jet is b-tagged you might want to keep the jet
#     cleanSelectedLeptons = True, #Whether to clean 'selectedLeptons' after disambiguation. Treat with care (= 'False') if running Jetanalyzer more than once
#     minLepPt = 10,
#     relaxJetId = True,
#     doPuId = True, # Not commissioned in 7.0.X
#     recalibrateJets = True, #'MC', # True, False, 'MC', 'Data'
#     applyL2L3Residual = True, # Switch to 'Data' when they will become available for Data
#     recalibrationType = "AK8PFchs",
#     mcGT     = "Spring16_25nsV6_MC",
#     dataGT   = "Spring16_25nsV6_DATA",
#     jecPath = "${CMSSW_BASE}/src/CMGTools/RootTools/data/jec/",
#     shiftJEC = 0, # set to +1 or -1 to apply +/-1 sigma shift to the nominal jet energies
#     smearJets = False,
#     shiftJER = 0, # set to +1 or -1 to get +/-1 sigma shifts
#     cleanJetsFromFirstPhoton = False,
#     cleanJetsFromTaus = False,
#     cleanJetsFromIsoTracks = False,
#     cleanAllJets    = True,
#     alwaysCleanPhotons     = True,
#     cleanGenJetsFromPhoton = True,
#     cleanJetsFromLeptons = True,
#     storeLowPtJets = False,
#     addJECShifts           = True,
#     calculateType1METCorrection  = True,
#     doQG = False,
#     do_mc_match = True,
#     collectionPostFix = "AK8",
#     calculateSeparateCorrections = True, # should be True if recalibrateJets is True, otherwise L1s will be inconsistent
#     type1METParams = { 'jetPtThreshold':15., 'skipEMfractionThreshold':0.9, 'skipMuons':True },
#     )

##____________________________________________________________________________||
# from CMGTools.ZGammaRatio.analyzers.AtFatJetAnalyzer import AtFatJetAnalyzer
# AtSubJetAna = cfg.Analyzer(
#     AtFatJetAnalyzer, name = 'AtSubJetAnalyzer',
#     jetCol = 'slimmedJetsAK8',
#     jets_in = 'cleanJetsAK8',
#     subjetCol = "SoftDrop",
#     jetPt = 100.,
#     jetEta = 5.,
#     jetLepDR = 0.4,
#     # v--- not implemented for AK8
#     #jetLepDR = 0.4,
#     #minLepPt = 10,
#     relaxJetId = False,
#     jetVerbose = False,
#     )

##____________________________________________________________________________||
from CMGTools.ZGammaRatio.analyzers.AtEventAttributesPrep import AtEventAttributesPrep
atEventAttributesPrep = cfg.Analyzer(
    AtEventAttributesPrep, name='atEventAttributesPrep',
    metnohf = False,
    electron_selection_id = ele_id_loose,
    electron_veto_id = ele_id_veto,
    muon_selection_id = mu_id_loose,
    photon_selection_id = pho_id_selection,
    )


##____________________________________________________________________________||
from CMGTools.ZGammaRatio.analyzers.AtEventAttributesPost import AtEventAttributesPost
atEventAttributesPost = cfg.Analyzer(
    AtEventAttributesPost, name='atEventAttributesPost',
    metnohf = False
    )

##____________________________________________________________________________||
from CMGTools.ZGammaRatio.analyzers.AtScribblerRunner import AtScribblerRunner
atScribblers = cfg.Analyzer(
    AtScribblerRunner, name='atScribblers',
    scribblers = [ ]
    )

##____________________________________________________________________________||
from CMGTools.ZGammaRatio.analyzers.AtEventSelectionRunner import AtEventSelectionRunner
atEventSelection = cfg.Analyzer(
    AtEventSelectionRunner, name='atEventSelection',
    function = lambda ev: True
    )

##____________________________________________________________________________||
from CMGTools.ZGammaRatio.treeContent.baseContent import *
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyAlphaT',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the
                                   # TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = susyAlphaT_globalVariables,
     globalObjects = susyAlphaT_globalObjects,
     collections = susyAlphaT_collections,
     isCompressed = 9,
    )

##____________________________________________________________________________||
def buildSequence(datamc, scribbler_options, buildEventSelection_options,
                  runPreProcessor = True, disableXC = False, relaxPhID = True):
    """
    datamc: 'data' or 'mc'
    scribbler_options: a dict with options for scribbler_configs()
    event_selection_options: a dict with options for event_selection()
    runPreProcessor: True or False
    disableXC: True or False for jet-lepton cross-cleaning
    """

    ##________________________________________________________________________||
    ## Modify the analyzers

    #photons
    photonAna.gammaID = pho_id_selection if not relaxPhID else pho_id_selection_fakeEnriched
    atEventAttributesPrep.photon_selection_id = pho_id_selection if not relaxPhID else pho_id_selection_fakeEnriched
    #leptons

    if disableXC:
        jetAna.jetLepArbitration    = (lambda jet,lepton: jet)
        jetAna.cleanSelectedLeptons = False

    ##________________________________________________________________________||
    ## sequence
    from CMGTools.ZGammaRatio.atlogic.buildScribblerPathForTreeProduction import buildScribblerPathForTreeProduction
    atScribblers.scribblers = buildScribblerPathForTreeProduction(**scribbler_options)

    from CMGTools.ZGammaRatio.atlogic.buildEventSelection import buildEventSelection
    atEventSelection.function = buildEventSelection(**buildEventSelection_options)

    sequence = [
        skimAna,
        jsonAna,
        triggerAna,
        vertexAna,
        atnVertCounter,
        pileUpAna,
        lheWeightAna,
        lheAna,
        genAna,
        # genHFAna,
        pdfwAna,
        # lepAna,
        #ttHLepSkim,
        # photonAna,
        # tauAna,
        # isoTrackAna,
        # jetAna,
        # metAna,
        # ttHCoreEventAna,
        # triggerFlagsAna,
        # eventFlagsAna,
        # badMuonAna,
        # badMuonAnaMoriond2017,
        # badCloneMuonAnaMoriond2017,
        # badChargedHadronAna,
        ###
        # atJetsJECVariations,
        # atJetsFwdJECVariations,
        # isoTrackNoMu,
        # isoTrackNoEle,
        # isoTrackNoMuEle,
        # atLheHTnoT,
        # atLheN,
        # atLheHTHistogram,
        ###
        # atMiscVarsCalculator,
        # ttHGenBinAna,
        #AtFatJetAna,
        #atFatJetsJECVariations,
        #AtSubJetAna,
        # HbheAnalyzer,
        ###
        atEventAttributesPrep,
        atScribblers,
        atEventSelection,
        atEventAttributesPost,
        ###
        treeProducer,
        ]

    if datamc == 'mc':
        if triggerAna in sequence: sequence.remove(triggerAna)
    else:
        if lheAna in sequence: sequence.remove(lheAna)
        if atLheHTnoT in sequence: sequence.remove(atLheHTnoT)
        if atLheN in sequence: sequence.remove(atLheN)
        if atLheHTHistogram in sequence: sequence.remove(atLheHTHistogram)

    return sequence

##__________________________________________________________________||
