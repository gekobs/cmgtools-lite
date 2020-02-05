import PhysicsTools.HeppyCore.framework.config as cfg
import os

##__________________________________________________________________||
jsonDir = "$CMSSW_BASE/src/CMGTools/ZGammaRatio/data/json/2016"
json_DCSONLY = os.path.join(jsonDir, 'json_DCSONLY.txt')
json_GoldenReReco = os.path.join(jsonDir, 'Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt')

##__________________________________________________________________||
triggers_JetHT          = ["HLT_PFHT800_v", "HLT_PFHT900_v"]
triggers_HTMHT          = ["HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v", "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v",
                           "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v", "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v",
                           "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v", "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v",
                           "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v", "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v",
                           "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v", "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v"]
triggers_MET            = ["HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v",
                           "HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v",
                           "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v",
                           "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v"]
triggers_SingleElectron = ["HLT_Ele22_WPLoose_Gsf_v",
                           "HLT_Ele23_WPLoose_Gsf_v",
                           "HLT_Ele25_WPTight_Gsf_v", "HLT_Ele25_eta2p1_WPTight_Gsf_v"
                           "HLT_Ele27_eta2p1_WPTight_Gsf_v", "HLT_Ele27_eta2p1_WPLoose_Gsf_v", "HLT_Ele27_WPTight_Gsf_v",
                           "HLT_Ele30_eta2p1_WPTight_Gsf_v", "HLT_Ele30_WPTight_Gsf_v",
                           "HLT_Ele32_eta2p1_WPTight_Gsf_v"  "HLT_Ele32_eta2p1_WPLoose_Gsf_v", "HLT_Ele32_WPTight_Gsf_v"]
triggers_SingleMuon     = ["HLT_IsoMu20_v", "HLT_IsoTkMu20_v",
                           "HLT_IsoMu22_v", "HLT_IsoTkMu22_v", "HLT_IsoMu22_eta2p1_v", "HLT_IsoTkMu22_eta2p1_v",
                           "HLT_IsoMu24_v", "HLT_IsoTkMu24_v", "HLT_IsoMu24_eta2p1_v", "HLT_IsoTkMu24_eta2p1_v", "HLT_Mu24_v", "HLT_TkMu24_v"
                           "HLT_IsoMu27_v", "HLT_IsoTkMu27_v"
                           "HLT_Mu50_v", "HLT_TkMu50_v"]
triggers_SinglePhoton   = ["HLT_Photon120_v",
                           "HLT_Photon165_HE10_v",
                           "HLT_Photon175_v",
                           "HLT_Photon250_NoHE_v"]
triggers_DoubleEG       = ["HLT_ECALHT800_v"]
triggers_zeroBias       = ["HLT_ZeroBias_v"]

##__________________________________________________________________||
## Run2016B
SingleMuon_Run2016B_17Jul2018_v1     = dict(name = "SingleMuon_Run2016B_17Jul2018_v1"    ,dataset = "/SingleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD"    , json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleMuon , user = "CMS" , pattern =".*root", useAAA=True)
SinglePhoton_Run2016B_17Jul2018_v1   = dict(name = "SinglePhoton_Run2016B_17Jul2018_v1"  ,dataset = "/SinglePhoton/Run2016B-17Jul2018_ver1-v1/MINIAOD"  , json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SinglePhoton , user = "CMS" , pattern =".*root", useAAA=True)
SingleElectron_Run2016B_17Jul2018_v1 = dict(name = "SingleElectron_Run2016B_17Jul2018_v1",dataset = "/SingleElectron/Run2016B-17Jul2018_ver1-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleElectron , user = "CMS" , pattern =".*root", useAAA=True)

componentList_Run2016B_17Jul2018_v1 = [
        SingleMuon_Run2016B_17Jul2018_v1,
        SinglePhoton_Run2016B_17Jul2018_v1,
        SingleElectron_Run2016B_17Jul2018_v1,
        ]

SingleMuon_Run2016B_17Jul2018_v2     = dict(name = "SingleMuon_Run2016B_17Jul2018_v2"    ,dataset = "/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD"    ,json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleMuon , user = "CMS" , pattern =".*root", useAAA=True)
SinglePhoton_Run2016B_17Jul2018_v2   = dict(name = "SinglePhoton_Run2016B_17Jul2018_v2"  ,dataset = "/SinglePhoton/Run2016B-17Jul2018_ver2-v1/MINIAOD"  ,json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SinglePhoton , user = "CMS" , pattern =".*root", useAAA=True)
SingleElectron_Run2016B_17Jul2018_v2 = dict(name = "SingleElectron_Run2016B_17Jul2018_v2",dataset = "/SingleElectron/Run2016B-17Jul2018_ver2-v1/MINIAOD",json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleElectron , user = "CMS" , pattern =".*root", useAAA=True)


componentList_Run2016B_17Jul2018_v2 = [
        SingleMuon_Run2016B_17Jul2018_v2,
        SinglePhoton_Run2016B_17Jul2018_v2,
        SingleElectron_Run2016B_17Jul2018_v2,
        ]

##__________________________________________________________________||
## Run2016C

SingleMuon_Run2016C_17Jul2018_v1 = dict(name = "SingleMuon_Run2016C_17Jul2018_v1" ,dataset = "/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD"    ,json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleMuon , user = "CMS" , pattern =".*root", useAAA=True)
SinglePhoton_Run2016C_17Jul2018_v1 = dict(name = "SinglePhoton_Run2016C_17Jul2018_v1" ,dataset = "/SinglePhoton/Run2016C-17Jul2018-v1/MINIAOD"  ,json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SinglePhoton , user = "CMS" , pattern =".*root", useAAA=True)
SingleElectron_Run2016C_17Jul2018_v1 = dict(name = "SingleElectron_Run2016C_17Jul2018_v1",dataset = "/SingleElectron/Run2016C-17Jul2018-v1/MINIAOD",json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleElectron , user = "CMS" , pattern =".*root", useAAA=True)

componentList_Run2016C_17Jul2018_v1 = [
        SingleMuon_Run2016C_17Jul2018_v1,
        SinglePhoton_Run2016C_17Jul2018_v1,
        SingleElectron_Run2016C_17Jul2018_v1,
        ]

##__________________________________________________________________||
## Run2016D

SingleMuon_Run2016D_17Jul2018_v1 = dict(name = "SingleMuon_Run2016D_17Jul2018_v1" ,dataset = "/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleMuon , user = "CMS" , pattern =".*root", useAAA=True)
SinglePhoton_Run2016D_17Jul2018_v1 = dict(name = "SinglePhoton_Run2016D_17Jul2018_v1" ,dataset = "/SinglePhoton/Run2016D-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SinglePhoton , user = "CMS" , pattern =".*root", useAAA=True)
SingleElectron_Run2016D_17Jul2018_v1 = dict(name = "SingleElectron_Run2016D_17Jul2018_v1" ,dataset = "/SingleElectron/Run2016D-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleElectron , user = "CMS" , pattern =".*root", useAAA=True)


componentList_Run2016D_17Jul2018_v1 = [
        SingleMuon_Run2016D_17Jul2018_v1,
        SinglePhoton_Run2016D_17Jul2018_v1,
        SingleElectron_Run2016D_17Jul2018_v1,

        ]

##__________________________________________________________________||
## Run2016E

SingleMuon_Run2016E_17Jul2018_v1 = dict(name = "SingleMuon_Run2016E_17Jul2018_v1" ,dataset = "/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleMuon , user = "CMS" , pattern =".*root", useAAA=True)
SinglePhoton_Run2016E_17Jul2018_v1 = dict(name = "SinglePhoton_Run2016E_17Jul2018_v1" ,dataset = "/SinglePhoton/Run2016E-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SinglePhoton , user = "CMS" , pattern =".*root", useAAA=True)
SingleElectron_Run2016E_17Jul2018_v1 = dict(name = "SingleElectron_Run2016E_17Jul2018_v1" ,dataset = "/SingleElectron/Run2016E-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleElectron , user = "CMS" , pattern =".*root", useAAA=True)


componentList_Run2016E_17Jul2018_v1 = [
        SingleMuon_Run2016E_17Jul2018_v1,
        SinglePhoton_Run2016E_17Jul2018_v1,
        SingleElectron_Run2016E_17Jul2018_v1,

        ]

##__________________________________________________________________||
## Run2016F

SingleMuon_Run2016F_17Jul2018_v1  = dict(name = "SingleMuon_Run2016F_17Jul2018_v1" ,dataset = "/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleMuon , user = "CMS" , pattern =".*root", useAAA=True)
SinglePhoton_Run2016F_17Jul2018_v1 = dict(name = "SinglePhoton_Run2016F_17Jul2018_v1" ,dataset = "/SinglePhoton/Run2016F-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SinglePhoton , user = "CMS" , pattern =".*root", useAAA=True)
SingleElectron_Run2016F_17Jul2018_v1 = dict(name = "SingleElectron_Run2016F_17Jul2018_v1" ,dataset = "/SingleElectron/Run2016F-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleElectron , user = "CMS" , pattern =".*root", useAAA=True)


componentList_Run2016F_17Jul2018_v1 = [
        SingleMuon_Run2016F_17Jul2018_v1,
        SinglePhoton_Run2016F_17Jul2018_v1,
        SingleElectron_Run2016F_17Jul2018_v1,

        ]

##__________________________________________________________________||
## Run2016G

SingleMuon_Run2016G_17Jul2018_v1 = dict(name = "SingleMuon_Run2016G_17Jul2018_v1" ,dataset = "/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleMuon , user = "CMS" , pattern =".*root", useAAA=True)
SinglePhoton_Run2016G_17Jul2018_v1 = dict(name = "SinglePhoton_Run2016G_17Jul2018_v1" ,dataset = "/SinglePhoton/Run2016G-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SinglePhoton , user = "CMS" , pattern =".*root", useAAA=True)
SingleElectron_Run2016G_17Jul2018_v1 = dict(name = "SingleElectron_Run2016G_17Jul2018_v1" ,dataset = "/SingleElectron/Run2016G-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleElectron , user = "CMS" , pattern =".*root", useAAA=True)


componentList_Run2016G_17Jul2018_v1 = [
        SingleMuon_Run2016G_17Jul2018_v1,
        SinglePhoton_Run2016G_17Jul2018_v1,
        SingleElectron_Run2016G_17Jul2018_v1,
      
        ]

##__________________________________________________________________||
## Run2016H

SingleMuon_Run2016H_17Jul2018_v1 = dict(name = "SingleMuon_Run2016H_17Jul2018_v1" ,dataset = "/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleMuon , user = "CMS" , pattern =".*root", useAAA=True)
SinglePhoton_Run2016H_17Jul2018_v1 = dict(name = "SinglePhoton_Run2016H_17Jul2018_v1" ,dataset = "/SinglePhoton/Run2016H-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SinglePhoton , user = "CMS" , pattern =".*root", useAAA=True)
SingleElectron_Run2016H_17Jul2018_v1 = dict(name = "SingleElectron_Run2016H_17Jul2018_v1" ,dataset = "/SingleElectron/Run2016H-17Jul2018-v1/MINIAOD", json = json_GoldenReReco, jsonFilter = False, run_range = None, triggers = triggers_SingleElectron , user = "CMS" , pattern =".*root", useAAA=True)

componentList_Run2016H_17Jul2018_v1 = [
        SingleMuon_Run2016H_17Jul2018_v1,
        SinglePhoton_Run2016H_17Jul2018_v1,
        SingleElectron_Run2016H_17Jul2018_v1,
        ]

##__________________________________________________________________||
if __name__ == "__main__":
    componentList =  [ ]
    componentList.extend(componentList_Run2016B_17Jul2018_v1)
    componentList.extend(componentList_Run2016B_17Jul2018_v2)
    componentList.extend(componentList_Run2016C_17Jul2018_v1)
    componentList.extend(componentList_Run2016D_17Jul2018_v1)
    componentList.extend(componentList_Run2016E_17Jul2018_v1)
    componentList.extend(componentList_Run2016F_17Jul2018_v1)
    componentList.extend(componentList_Run2016G_17Jul2018_v1)
    componentList.extend(componentList_Run2016H_17Jul2018_v1)

    
    from CMGTools.ZGammaRatio.components.ComponentCreator import ComponentCreator
    kreator = ComponentCreator()
    components = [kreator.makeDataComponent(**s) for s in componentList]
    import sys
    if "test" in sys.argv:
        from CMGTools.ZGammaRatio.components.ComponentCreator import testSamples
        testSamples(components)