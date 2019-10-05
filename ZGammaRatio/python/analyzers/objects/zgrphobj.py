#!/bin/env python
from PhysicsTools.Heppy.analyzers.core.autovars import *
from PhysicsTools.Heppy.analyzers.objects.autophobj import *

jetTypeZgr = NTupleObjectType("", baseObjectTypes = [jetType], variables = [
    NTupleVariable("chHEF",    lambda x : x.chargedHadronEnergyFraction(), float, mcOnly = False, help = "chargedHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("neHEF",    lambda x : x.neutralHadronEnergyFraction(), float, mcOnly = False, help = "neutralHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("phEF",     lambda x: x.photonEnergyFraction(),         float, mcOnly = False, help = "photonEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("eEF",      lambda x: x.electronEnergyFraction(),       float, mcOnly = False, help = "electronEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("muEF",     lambda x: x.muonEnergyFraction(),           float, mcOnly = False, help = "muonEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("HFHEF",    lambda x: x.HFHadronEnergyFraction(),       float, mcOnly = False, help = "HFHadronEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("HFEMEF",   lambda x: x.HFEMEnergyFraction(),           float, mcOnly = False, help = "HFEMEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("chHMult",  lambda x: x.chargedHadronMultiplicity(),    int,   mcOnly = False, help = "chargedHadronMultiplicity from PFJet.h"),
    NTupleVariable("neHMult",  lambda x: x.neutralHadronMultiplicity(),    int,   mcOnly = False, help = "neutralHadronMultiplicity from PFJet.h"),
    NTupleVariable("phMult",   lambda x: x.photonMultiplicity(),           int,   mcOnly = False, help = "photonMultiplicity from PFJet.h"),
    NTupleVariable("eMult",    lambda x: x.electronMultiplicity(),         int,   mcOnly = False, help = "electronMultiplicity from PFJet.h"),
    NTupleVariable("muMult",   lambda x: x.muonMultiplicity(),             int,   mcOnly = False, help = "muonMultiplicity from PFJet.h"),
    NTupleVariable("HFHMult",  lambda x: x.HFHadronMultiplicity(),         int,   mcOnly = False, help = "HFHadronMultiplicity from PFJet.h"),
    NTupleVariable("HFEMMult", lambda x: x.HFEMMultiplicity(),             int,   mcOnly = False, help = "HFEMMultiplicity from PFJet.h"),
    ])
