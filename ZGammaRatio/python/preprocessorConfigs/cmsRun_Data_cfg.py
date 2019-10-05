import FWCore.ParameterSet.Config as cms
import os

##__________________________________________________________________||
maxEvents = -1
GT = '74X_dataRun2_Prompt_v2'
jecEra='Summer15_25nsV6_DATA'
jecDBFile ='$CMSSW_BASE/src/CMGTools/RootTools/data/jec/' + jecEra + '.db'
uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/' + jecEra + '_UncertaintySources_AK4PFchs.txt'

isData = True
removeResiduals = False
json = '$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/json_DCSONLY.txt'

usePrivateSQlite = True if jecDBFile else False

##__________________________________________________________________||
process = cms.Process("RERUN")

##__________________________________________________________________||
# Load the standard set of configuration modules
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

##__________________________________________________________________||
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

##__________________________________________________________________||
process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(False),
    wantSummary = cms.untracked.bool(True)
)

##__________________________________________________________________||
process.maxEvents = cms.untracked.PSet(
   input = cms.untracked.int32(maxEvents)
)

##__________________________________________________________________||
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag.globaltag = cms.string(GT)

if usePrivateSQlite:
    from CondCore.DBCommon.CondDBSetup_cfi import *
    process.jec = cms.ESSource(
        "PoolDBESSource", CondDBSetup,
        connect = cms.string('sqlite_file:'+ os.path.expandvars(jecDBFile)),
        toGet = cms.VPSet(
            cms.PSet(
                record = cms.string("JetCorrectionsRecord"),
                tag = cms.string("JetCorrectorParametersCollection_" + jecEra + "_AK4PF"),
                label= cms.untracked.string("AK4PF")
                ),
            cms.PSet(
                record = cms.string("JetCorrectionsRecord"),
                tag = cms.string("JetCorrectorParametersCollection_" + jecEra + "_AK4PFchs"),
                label = cms.untracked.string("AK4PFchs")
                ),
            )
                               )
    process.es_prefer_jec = cms.ESPrefer("PoolDBESSource", 'jec')

##__________________________________________________________________||
fname = '/store/data/Run2015C/HTMHT/MINIAOD/PromptReco-v1/000/254/852/00000/78B9F88B-944B-E511-82F0-02163E0133B5.root'
# fname = 'root://cms-xrd-global.cern.ch/%s' % fname

##__________________________________________________________________||
import FWCore.PythonUtilities.LumiList as LumiList

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring([ fname ])
)

if json:
    process.source.lumisToProcess = LumiList.LumiList(filename = os.path.expandvars(json)).getVLuminosityBlockRange()

##__________________________________________________________________||
process.sequence_filters = cms.Sequence( )

from HLTrigger.HLTfilters.hltHighLevel_cfi import *
process.HLTpaths = hltHighLevel.clone(
    throw = cms.bool(False),
    HLTPaths = [
        "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v*", # HTMHT
        "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v*", # HTMHT
        "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v*", # HTMHT
        "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v*", # HTMHT
        "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v*", # HTMHT
        "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v*", # HTMHT
        "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v*", # HTMHT
        "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v*", # HTMHT
        "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v*", # HTMHT
        "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v*", # HTMHT
        "HLT_PFHT800_v*", # JetHT
        "HLT_PFMET90_PFMHT90_IDTight_v*", # MET
        "HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*", # MET
        "HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*", # MET
        "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*", # MET
        "HLT_PFMET120_v*", # MET
        "HLT_IsoMu20_v*",        # SingleMuon
        "HLT_IsoTkMu20_v*",      # SingleMuon
        "HLT_IsoMu17_eta2p1_v*", # SingleMuon
        "HLT_IsoMu24_eta2p1_v*", # SingleMuon
        "HLT_Mu24_v*", # SingleMuon
        "HLT_TkMu24_v*", # SingleMuon
        "HLT_Ele22_WPLoose_Gsf_v*", # SingleElectron
        "HLT_Ele23_WPLoose_Gsf_v*", # SingleElectron
        "HLT_Ele27_eta2p1_WPLoose_Gsf_v*", # SingleElectron
        "HLT_Photon90_v*",      # Photon
        "HLT_Photon120_v*",     # Photon
        "HLT_Photon165_HE10_v*" # Photon
        "HLT_Photon175_v*",     # Photon
        ]
    )

process.sequence_filters += process.HLTpaths

##__________________________________________________________________||
process.highPtJet = cms.EDFilter(
    "PATJetSelector",
    src = cms.InputTag("slimmedJets"),
    cut = cms.string("pt > 80"),
    filter = cms.bool(True)
    )

process.sequence_filters += process.highPtJet

##__________________________________________________________________||
process.noHFCands = cms.EDFilter(
    "CandPtrSelector",
    src=cms.InputTag("packedPFCandidates"),
    cut=cms.string("abs(pdgId)!=1 && abs(pdgId)!=2 && abs(eta)<3.0")
    )

from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
runMetCorAndUncFromMiniAOD(process,
                           isData = isData,
                           pfCandColl = cms.InputTag("noHFCands"),
                           # jecUncFile = uncFile,
                           postfix = "NoHF"
                           )

process.sequence_metnohf = cms.Sequence(
    process.noHFCands +
    process.pfMetNoHF +
    process.patPFMetNoHF +
    process.pfCHSNoHF +
    process.ak4PFJetsCHSNoHF +
    process.patJetCorrFactorsNoHF +
    process.patJetsNoHF +
    process.patPFMetT1T2CorrNoHF +
    process.patPFMetT1NoHF
    )

##__________________________________________________________________||
if removeResiduals:
    process.patPFMetT1T2Corr.jetCorrLabelRes = cms.InputTag("L3Absolute")
    process.patPFMetT1T2SmearCorr.jetCorrLabelRes = cms.InputTag("L3Absolute")
    process.patPFMetT2Corr.jetCorrLabelRes = cms.InputTag("L3Absolute")
    process.patPFMetT2SmearCorr.jetCorrLabelRes = cms.InputTag("L3Absolute")
    process.shiftedPatJetEnDown.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
    process.shiftedPatJetEnUp.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")

    process.patPFMetT1T2CorrNoHF.jetCorrLabelRes = cms.InputTag("L3Absolute")
    process.patPFMetT1T2SmearCorrNoHF.jetCorrLabelRes = cms.InputTag("L3Absolute")
    process.patPFMetT2CorrNoHF.jetCorrLabelRes = cms.InputTag("L3Absolute")
    process.patPFMetT2SmearCorrNoHF.jetCorrLabelRes = cms.InputTag("L3Absolute")
    process.shiftedPatJetEnDownNoHF.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
    process.shiftedPatJetEnUpNoHF.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")

##__________________________________________________________________||
process.p = cms.Path(
    process.sequence_filters *
    process.sequence_metnohf
)

##__________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring(
        "keep *_patPFMetT1NoHF_*_*",
        ),
    fileName = cms.untracked.string('corMETMiniAOD.root'),
    dropMetaData = cms.untracked.string('ALL'),
    compressionLevel = cms.untracked.int32(9),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring("p")
        )
    )

process.endpath = cms.EndPath(process.out)

##__________________________________________________________________||
