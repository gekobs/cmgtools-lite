import FWCore.ParameterSet.Config as cms
import os

##__________________________________________________________________||
maxEvents = -1
GT = '94X_mcRun2_asymptotic_v3'
jecEra='Summer16_07Aug2017_V11_MC'
jecDBFile ='$CMSSW_BASE/src/CMGTools/RootTools/data/jec/' + jecEra + '.db'
uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/' + jecEra + '_UncertaintySources_AK4PFchs.txt'

isData = False
removeResiduals = False

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
fname = '/store/mc/RunIISpring15DR74/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/20000/0C0C9631-EC33-E511-B1C0-C4346BC7EE18.root'
# fname = '/store/mc/RunIISpring15DR74/ADDGravToGG_MS-6000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/20000/76CA81A9-1024-E511-8D9F-3417EBE6471D.root'
# fname = 'root://cms-xrd-global.cern.ch/%s' % fname

##__________________________________________________________________||
import FWCore.PythonUtilities.LumiList as LumiList

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring([ fname ])
)

##__________________________________________________________________||
process.sequence_filters = cms.Sequence( )

##__________________________________________________________________||
process.highPtJet = cms.EDFilter(
    "PATJetSelector",
    src = cms.InputTag("slimmedJets"),
    cut = cms.string("pt > 80"),
    filter = cms.bool(True)
    )

# process.sequence_filters += process.highPtJet

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

process.patPFMetNoHF.addGenMET = cms.bool(False)

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
