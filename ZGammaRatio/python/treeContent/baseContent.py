from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *
from CMGTools.ZGammaRatio.analyzers.objects.zgrphobj import *

susyAlphaT_globalVariables = [
    NTupleVariable("rho",          lambda ev: ev.rho,          float, help="kt6PFJets rho"),
    NTupleVariable("rhoCN",        lambda ev: ev.rhoCN,        float, help="fixed grid rho central neutral"),
    NTupleVariable("nVert",        lambda ev: ev.nVert,        int,   help="Number of good vertices"),

    # MET filters
    ##----------------------------------------
    NTupleVariable("Flag_badMuonFilter",          lambda ev: ev.badMuon,          help="bad muon filter decision"),
    NTupleVariable("Flag_badChargedHadronFilter", lambda ev: ev.badChargedHadron, help="bad charged hadron filter decision"),

    # Moriond17 bad muon filters (final recipe compared with re-MINIAOD flags)
    ##----------------------------------------
    NTupleVariable("Flag_badMuonMoriond2017",             lambda ev: ev.badMuonMoriond2017,                  int, help="bad muon found in event (Moriond 2017 filter)"),
    NTupleVariable("Flag_badCloneMuonMoriond2017",        lambda ev: ev.badCloneMuonMoriond2017,             int, help="clone muon found in event (Moriond 2017 filter)"),
    NTupleVariable("badCloneMuonMoriond2017_maxPt",       lambda ev: max(mu.pt() for mu in ev.badCloneMuonMoriond2017_badMuons) if not ev.badCloneMuonMoriond2017 else 0, help="max pt of any clone muon found in event (Moriond 2017 filter)"),
    NTupleVariable("badNotCloneMuonMoriond2017_maxPt",    lambda ev: max((mu.pt() if mu not in ev.badCloneMuonMoriond2017_badMuons else 0) for mu in ev.badMuonMoriond2017_badMuons) if not ev.badMuonMoriond2017 else 0, help="max pt of any bad non-clone muon found in event (Moriond 2017 filter)"),

    # HBHE Noise filters
    ##----------------------------------------
    NTupleVariable("hbheMaxZeros",                  lambda ev : ev.hbheMaxZeros),
    NTupleVariable("hbheMaxHPDHits",                lambda ev : ev.hbheMaxHPDHits),
    NTupleVariable("hbheMaxHPDNoOtherHits",         lambda ev : ev.hbheMaxHPDNoOtherHits),
    NTupleVariable("hbheHasBadRBXTS4TS5",           lambda ev : ev.hbheHasBadRBXTS4TS5),
    NTupleVariable("hbheGoodJetFoundInLowBVRegion", lambda ev : ev.hbheGoodJetFoundInLowBVRegion),
    NTupleVariable("hbheHasBadRBXRechitR45Loose",   lambda ev : ev.hbheHasBadRBXRechitR45Loose),
    NTupleVariable("hbheFilterNew",                 lambda ev : ev.hbheFilterNew),
    # NTupleVariable("hbheFilterNewTight",            lambda ev : ev.hbheFilterNewTight),
    NTupleVariable("hbheFilterIso",                 lambda ev : ev.hbheFilterIso),

    # Gen quantities
    ##----------------------------------------
    NTupleVariable("genBin",                  lambda ev : ev.genBin,    mcOnly=True, help="Generator level binning quantity"),
    NTupleVariable("genQScale",               lambda ev : ev.genQScale, mcOnly=True, help="Generator level binning quantity, QScale"),
    NTupleVariable("nPromptGenPhotons",       lambda ev : ev.nPromptGenPhotons if hasattr(ev, "nPromptGenPhotons") else 0,             int, mcOnly=True, help="number of gen prompt photons"),
    NTupleVariable("nPromptDirectGenPhotons", lambda ev : ev.nPromptDirectGenPhotons if hasattr(ev, "nPromptDirectGenPhotons") else 0, int, mcOnly=True, help="number of gen prompt direct photons"),

    NTupleVariable("lheHT",         lambda ev: ev.lheHT if hasattr(ev, "lheHT") else 0, mcOnly=True, help="LHE HT(q + g)"),
    NTupleVariable("lheHTIncoming", lambda ev: ev.lheHTIncoming, mcOnly=True, help="Restricts HT computation to particles that have status<0 mothers"),
    NTupleVariable("lheNj",         lambda ev: ev.lheNj,         mcOnly=True, help="Number of LHE gluons and quarks"),
    NTupleVariable("lheNb",         lambda ev: ev.lheNb,         mcOnly=True, help="Number of LHE b quarks"),
    NTupleVariable("lheNc",         lambda ev: ev.lheNc,         mcOnly=True, help="Number of LHE c quarks"),
    NTupleVariable("lheNl",         lambda ev: ev.lheNl,         mcOnly=True, help="Number of LHE u,d,s quarks"),
    NTupleVariable("lheV_pt",       lambda ev: ev.lheV_pt,       mcOnly=True, help="LHE vector boson (W,Z,gamma) pT"),
    NTupleVariable("lheHTnoT",      lambda ev: ev.lheHTnoT,      mcOnly=True, help="LHE HT(q + g) excluding contributions from top quarks"),

    NTupleVariable("originalWeight", lambda ev : ev.LHE_originalWeight, mcOnly=True, help="central event weight at LHE level (originalXWGTUP)"),

    # Energy sums (RECO)
    ##----------------------------------------
    NTupleVariable("ht40",        lambda ev : ev.ht40,        help="H_{T} computed from only jets (with |eta|<3, pt > 40 GeV)"),
    NTupleVariable("ht40JECUp",   lambda ev : ev.ht40JECUp,   help="H_{T} computed from only jets with JEC up (with |eta|<3, pt > 40 GeV)"),
    NTupleVariable("ht40JECDown", lambda ev : ev.ht40JECDown, help="H_{T} computed from only jets with JEC down (with |eta|<3, pt > 40 GeV)"),

    NTupleVariable("mht40_pt",        lambda ev : ev.mht40_pt,        help="H_{T}^{miss} computed from only jets (with |eta|<3.0, pt > 40 GeV)"),
    NTupleVariable("mht40JECUp_pt",   lambda ev : ev.mht40JECUp_pt,   help="H_{T}^{miss} computed from only jets with JEC up (with |eta|<3.0, pt > 40 GeV)"),
    NTupleVariable("mht40JECDown_pt", lambda ev : ev.mht40JECDown_pt, help="H_{T}^{miss} computed from only jets with JEC down (with |eta|<3.0, pt > 40 GeV)"),
    NTupleVariable("mht40_phi",       lambda ev : ev.mhtPhiJet40j,    help="H_{T}^{miss} #phi computed from only jets (with |eta|<3.0, pt > 40 GeV)"),

    NTupleVariable("met_caloPt",    lambda ev : ev.met.caloMETPt(),    help="calo met p_{T}"),
    NTupleVariable("met_caloPhi",   lambda ev : ev.met.caloMETPhi(),   help="calo met phi"),
    NTupleVariable("met_caloSumEt", lambda ev : ev.met.caloMETSumEt(), help="calo met sumEt"),

    # Energy sums (GEN)
    ##----------------------------------------
    NTupleVariable("genHt40",      lambda ev : ev.htGenJet40j,     mcOnly=True, help="H_{T} computed from only gen jets (with |eta|<3, pt > 40 GeV)"),
    NTupleVariable("genMht40_pt",  lambda ev : ev.mhtGenJet40j,    mcOnly=True, help="H_{T}^{miss} computed from only gen jets (with |eta|<3.0, pt > 40 GeV)"),
    NTupleVariable("genMht40_phi", lambda ev : ev.mhtPhiGenJet40j, mcOnly=True, help="H_{T}^{miss} #phi computed from only gen jets (with |eta|<3.0, pt > 40 GeV)"),

    ##----------------------------------------
    # Physics object multplicities
    ##----------------------------------------
    NTupleVariable("nLheElectrons", lambda ev: ev.nLheElectrons, int, mcOnly = True, help = "# electrons in LHE"),
    NTupleVariable("nLheMuons",     lambda ev: ev.nLheMuons,     int, mcOnly = True, help = "# muons in LHE"),
    NTupleVariable("nLheTaus",      lambda ev: ev.nLheTaus,      int, mcOnly = True, help = "# taus in LHE"),

    NTupleVariable("nJet40",  lambda ev: ev.nJet40,  int, help="Number of jets with pt > 40, |eta|<3.0"),
    NTupleVariable("nJet100", lambda ev: ev.nJet100, int, help="Number of jets with pt > 100, |eta|<3.0"),
    NTupleVariable("nBJet40", lambda ev: ev.nBJet40, int, help="Number of jets with pt > 40 passing CSV medium"),

    NTupleVariable("nJet40JECUp",  lambda ev: ev.nJet40JECUp,  int, help="Number of jets with JEC up with pt > 40, |eta|<3.0"),
    NTupleVariable("nJet100JECUp", lambda ev: ev.nJet100JECUp, int, help="Number of jets with JEC up with pt > 100, |eta|<3.0"),
    NTupleVariable("nBJet40JECUp", lambda ev: ev.nBJet40JECUp, int, help="Number of jets with JEC up with pt > 40 passing CSV medium"),

    NTupleVariable("nJet40JECDown",  lambda ev: ev.nJet40JECDown,  int, help="Number of jets with JEC down with pt > 40, |eta|<3.0"),
    NTupleVariable("nJet100JECDown", lambda ev: ev.nJet100JECDown, int, help="Number of jets with JEC down with pt > 100, |eta|<3.0"),
    NTupleVariable("nBJet40JECDown", lambda ev: ev.nBJet40JECDown, int, help="Number of jets with JEC down with pt > 40 passing CSV medium"),

    # control sample variables
    ##--------------------------------------------------
    NTupleVariable("mtw",         lambda ev: ev.mtw,         help="mt(l,met)"),
    NTupleVariable("mtwTau",      lambda ev: ev.mtwTau,      help="mt(tau,met)"),
    NTupleVariable("mtwIsoTrack", lambda ev: ev.mtwIsoTrack, help="mt(isoTrack,met)"),
    NTupleVariable("mll",         lambda ev: ev.mll,         help="Invariant mass of the two lead leptons"),

    NTupleVariable("cutflowId", lambda ev: ev.cutflowId, int, help="1: Signal, 2: SingleMu, 3: DoubleMu, 4: SingleEle, 5: DoubleEle, 6: SinglePhoton, -1: other"),

    NTupleVariable("nPhotonsVeto",          lambda ev: ev.nPhotonsVeto,          int, help="# of photons for veto"),
    NTupleVariable("nPhotonsSelection",     lambda ev: ev.nPhotonsSelection,     int, help="# of photons for selection"),
    NTupleVariable("nMuonsVeto",            lambda ev: ev.nMuonsVeto,            int, help="# of muons for veto"),
    NTupleVariable("nMuonsSelection",       lambda ev: ev.nMuonsSelection,       int, help="# of muons for selection"),
    NTupleVariable("nElectronsVeto",        lambda ev: ev.nElectronsVeto,        int, help="# of electrons for veto"),
    NTupleVariable("nElectronsLoose",       lambda ev: ev.nElectronsLoose,       int, help="# of electrons for loose"),
    NTupleVariable("nElectronsSelection",   lambda ev: ev.nElectronsSelection,   int, help="# of electrons for selection"),
    NTupleVariable("nIsoTracksVeto",        lambda ev: ev.nIsoTracksVeto,        int, help="# of isolated tracks for veto"),
    NTupleVariable("nIsoTracksNoMuVeto",    lambda ev: ev.nIsoTracksNoMuVeto,    int, help="# of isolated tracks without muons for veto"),
    NTupleVariable("nIsoTracksNoEleVeto",   lambda ev: ev.nIsoTracksNoEleVeto,   int, help="# of isolated tracks without electrons for veto"),
    NTupleVariable("nIsoTracksNoMuEleVeto", lambda ev: ev.nIsoTracksNoMuEleVeto, int, help="# of isolated tracks without electrons and muons for veto"),

    # NTupleVariable("nJet40failedId",   lambda ev: ev.nJet40failedId,   int, help="# of jets w/ pT > 40 w/ x-cleaning that failed the jet ID"),
    NTupleVariable("nJet40Fwd",        lambda ev: ev.nJet40Fwd,        int, help="# of forward jets w/ pT > 40 w/ x-cleaning"),
    NTupleVariable("nJet40FwdJECUp",   lambda ev: ev.nJet40FwdJECUp,   int, help="# of forward jets with JEC up w/ pT > 40 w/ x-cleaning"),
    NTupleVariable("nJet40FwdJECDown", lambda ev: ev.nJet40FwdJECDown, int, help="# of forward jets with JEC down w/ pT > 40 w/ x-cleaning"),

    NTupleVariable("minDelRJetMu",            lambda ev: ev.minDelRJetMu,     float, help="min deltaR among all pairs of jets and muons"),
    NTupleVariable("minDelRJetMuJECUp",       lambda ev: ev.minDelRJetMu,     float, help="min deltaR among all pairs of jets with JEC up and muons"),
    NTupleVariable("minDelRJetMuJECDown",     lambda ev: ev.minDelRJetMu,     float, help="min deltaR among all pairs of jets with JEC down and muons"),
    NTupleVariable("minDelRJetEle",           lambda ev: ev.minDelRJetEle,    float, help="min deltaR among all pairs of jets and electrons"),
    NTupleVariable("minDelRJetEleJECUp",      lambda ev: ev.minDelRJetEle,    float, help="min deltaR among all pairs of jets with JEC up and electrons"),
    NTupleVariable("minDelRJetEleJECDown",    lambda ev: ev.minDelRJetEle,    float, help="min deltaR among all pairs of jets with JEC down and electrons"),
    NTupleVariable("minDelRJetPhoton",        lambda ev: ev.minDelRJetPhoton, float, help="min deltaR among all pairs of jets and photons"),
    NTupleVariable("minDelRJetPhotonJECUp",   lambda ev: ev.minDelRJetPhoton, float, help="min deltaR among all pairs of jets with JEC up and photons"),
    NTupleVariable("minDelRJetPhotonJECDown", lambda ev: ev.minDelRJetPhoton, float, help="min deltaR among all pairs of jets with JEC down and photons"),
]


susyAlphaT_globalObjects = {
    "met"         : NTupleObject("met",         metType,        help="PF E_{T}^{miss}, after type 1 corrections"),
    "metNoMu"     : NTupleObject("metNoMu",     fourVectorType, help="met computed with muon momentum substracted"),
    "metNoEle"    : NTupleObject("metNoEle",    fourVectorType, help="met computed with electron momentum substracted"),
    "metNoPhoton" : NTupleObject("metNoPhoton", fourVectorType, help="met computed with photon momentum substracted"),
    # "metNoMuEle"  : NTupleObject("metNoMuEle", fourVectorType, help="met computed with muon and electron momentum substracted"),
}


susyAlphaT_collections = {
    "cleanJets":    NTupleCollection("jet",    jetTypeZgr, 100, help="all jets (w/ x-cleaning, w/ ID applied w/o PUID applied pt > 25 (JEC up) |eta| < 3) , sorted by pt", filter=lambda l: l.pt()/l.corr*l.corrJECUp>25  ),
    "cleanJetsFwd": NTupleCollection("jetFwd", jetTypeZgr, 100, help="all jets (w/ x-cleaning, w/ ID applied w/o PUID applied pt > 40 |eta| >= 3) , sorted by pt",         filter=lambda l: l.pt()>40  ),

    # Photons
    "selectedPhotons": NTupleCollection("gamma", photonType, 50, help="photons with pt > 25 and loose cut based ID"),

    # Leptons
    "selectedMuons":     NTupleCollection("muon", leptonTypeExtra, 50, help="Muons selected by the analysis"),
    "selectedElectrons": NTupleCollection("ele",  leptonTypeExtra, 50, help="Electrons selected by the analysis"),
    "selectedTaus":      NTupleCollection("tau",  tauType,    50, help="Taus after the preselection"),

    # Isotracks
    "selectedIsoTrack": NTupleCollection("isoTrack", isoTrackType, 50, help="isoTrack, sorted by pt"),

    #Gen collections
    #"genParticles":     NTupleCollection("allGenPart",    genParticleWithMotherId,  200, help="all pruned genparticles"),
    "cleanGenJets":     NTupleCollection("genJet",        genParticleType,          10,  help="Generated jets (cleaned)", filter=lambda j: j.pt()>15 ),
    "genPhotons":       NTupleCollection("genPhoton",     genPhotonType,            10,  help="Generated photons"),
    "genleps":          NTupleCollection("genLep",        genParticleWithLinksType, 10,  help="Generated leptons (e/mu) from W/Z decays"),
    "gentauleps":       NTupleCollection("genLepFromTau", genParticleWithLinksType, 10,  help="Generated leptons (e/mu) from decays of taus from W/Z/h decays"),
    "gentaus":          NTupleCollection("genTau",        genParticleWithLinksType, 10,  help="Generated leptons (tau) from W/Z decays"),
    "generatorSummary": NTupleCollection("GenPart",       genParticleWithLinksType, 100, help="Hard scattering particles, with ancestry and links"),

    # dR jet lep for each lepton
    "minDeltaRLepJet": NTupleCollection("minDeltaRLepJet", objectFloat, 10, help="Min deltaR between a lepton and all the jets"),
    "minDeltaRPhoJet": NTupleCollection("minDeltaRPhoJet", objectFloat, 10, help="Min deltaR between a photon and all the jets"),

    #"cleanJetsAK8":   NTupleCollection("fatjets",       fatJetType, 50, help="fat jet info", filter=lambda l: l.pt() > 175.0),
    #"fatJetsSubJets": NTupleCollection("fatjetSubjets", subJetType, 50, help="sub jet info", filter=lambda sj: sj.parentJet.pt() > 175),

    # LHE weights
    "LHE_weights": NTupleCollection("LHEweight", weightsInfoType, 1000, mcOnly=True, help="LHE weight info"),
    }
