
##__________________________________________________________________||
# Signal triggers
signalTriggerBits = {
    # Primary
    "PFHT200_DiPFJetAve90_PFAlphaT0p57" : ["HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v"],
    "PFHT250_DiPFJetAve90_PFAlphaT0p55" : ["HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v"],
    "PFHT300_DiPFJetAve90_PFAlphaT0p53" : ["HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v"],
    "PFHT350_DiPFJetAve90_PFAlphaT0p52" : ["HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v"],
    "PFHT400_DiPFJetAve90_PFAlphaT0p51" : ["HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v"],
    # Backup
    "PFHT200_DiPFJetAve90_PFAlphaT0p63" : ["HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v"],
    "PFHT250_DiPFJetAve90_PFAlphaT0p58" : ["HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v"],
    "PFHT300_DiPFJetAve90_PFAlphaT0p54" : ["HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v"],
    "PFHT350_DiPFJetAve90_PFAlphaT0p53" : ["HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v"],
    "PFHT400_DiPFJetAve90_PFAlphaT0p52" : ["HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v"],
    # HT Primary
    "PFHT800"                           : ["HLT_PFHT800_v"],
    # HT Backup
    "PFHT900"                           : ["HLT_PFHT900_v"],
    }

# Monojet triggers
monojetTriggerBits   = {
    "PFMETNoMu90_PFMHTNoMu90_IDTight"   : ["HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v"],
    "PFMETNoMu100_PFMHTNoMu100_IDTight" : ["HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v"],
    "PFMETNoMu110_PFMHTNoMu110_IDTight" : ["HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v"],
    "PFMETNoMu120_PFMHTNoMu120_IDTight" : ["HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v"],
    "PFMET170_NoiseCleaned"             : ["HLT_PFMET170_NoiseCleaned_v"],
}

##__________________________________________________________________||
# Muon triggers
muonTriggerBits = {
    "IsoMu27_eta2p1"   : ["HLT_IsoMu27_eta2p1_v"],
    "IsoMu27"          : ["HLT_IsoMu27_v"],
    "IsoTkMu27"        : ["HLT_IsoTkMu27_v"],
    "IsoMu24_eta2p1"   : ["HLT_IsoMu24_eta2p1_v"],
    "IsoTkMu24_eta2p1" : ["HLT_IsoTkMu24_eta2p1_v"],
    "IsoMu24"          : ["HLT_IsoMu24_v"],
    "IsoTkMu24"        : ["HLT_IsoTkMu24_v"],
    "IsoMu20"          : ["HLT_IsoMu20_v"],
    "IsoTkMu20"        : ["HLT_IsoTkMu20_v"],
    "IsoMu22_eta2p1"   : ["HLT_IsoMu22_eta2p1_v"],
    "IsoTkMu22_eta2p1" : ["HLT_IsoTkMu22_eta2p1_v"],
    "IsoMu22"          : ["HLT_IsoMu22_v"],
    "IsoTkMu22"        : ["HLT_IsoTkMu22_v"],
    "Mu24"             : ["HLT_Mu24_v"],
    "TkMu24"           : ["HLT_TkMu24_v"],
    "TkMu50"           : ["HLT_TkMu50_v"],
    "Mu50"             : ["HLT_Mu50_v"],
}

##__________________________________________________________________||
# Electron triggers
electronTriggerBits = { 
    "Ele32_eta2p1_WPLoose_Gsf": ["HLT_Ele32_eta2p1_WPLoose_Gsf_v"],
    "Ele32_WPTight_Gsf"       : ["HLT_Ele32_WPTight_Gsf_v"],
    "Ele32_eta2p1_WPTight_Gsf": ["HLT_Ele32_eta2p1_WPTight_Gsf_v"], 
    "Ele30_WPTight_Gsf"       : ["HLT_Ele30_WPTight_Gsf_v"], 
    "Ele30_eta2p1_WPTight_Gsf": ["HLT_Ele30_eta2p1_WPTight_Gsf_v"],
    "Ele27_WPTight_Gsf"       : ["HLT_Ele27_WPTight_Gsf_v"],
    "Ele27_eta2p1_WPLoose_Gsf": ["HLT_Ele27_eta2p1_WPLoose_Gsf_v"],
    "Ele27_eta2p1_WPTight_Gsf": ["HLT_Ele27_eta2p1_WPTight_Gsf_v"],
    "Ele25_WPTight_Gsf"       : ["HLT_Ele25_WPTight_Gsf_v"], 
    "Ele25_eta2p1_WPTight_Gsf": ["HLT_Ele25_eta2p1_WPTight_Gsf_v"], 
    "Ele23_WPLoose_Gsf"       : ["HLT_Ele23_WPLoose_Gsf_v"],
}

##__________________________________________________________________||
# Photon triggers
photonTriggerBits = {
    "Photon250_NoHE"     : ["HLT_Photon250_NoHE_v"],
    "Photon175"          : ["HLT_Photon175_v"],
    "Photon165_HE10"     : ["HLT_Photon165_HE10_v"],
}

# Photon alternative triggers
photonAlternativeTriggerBits = { 
    "ECALHT800"          : ["HLT_ECALHT800_v"],
    "CaloJet500_NoJetID" : ["HLT_CaloJet500_NoJetID_v"],
    "PFJet450"           : ["HLT_PFJet450_v"],
    "PFJet500"           : ["HLT_PFJet500_v"],
}

##__________________________________________________________________||
# Hadronic control triggers
hadronicTriggerBits = {
    "PFHT200" : ["HLT_PFHT200_v"],
    "PFHT250" : ["HLT_PFHT250_v"],
    "PFHT300" : ["HLT_PFHT300_v"],
    "PFHT350" : ["HLT_PFHT350_v"],
    "PFHT400" : ["HLT_PFHT400_v"],
    "PFHT200_PFAlphaT0p51" : ["HLT_PFHT200_PFAlphaT0p51_v"],
}

##__________________________________________________________________||
# Comissioning
comissioningTriggerBits = {
    "PFHT475" : ["HLT_PFHT475_v"], 
    "PFHT600" : ["HLT_PFHT600_v"], 
    "PFHT650" : ["HLT_PFHT650_v"], 
}

##__________________________________________________________________||
