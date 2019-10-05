from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer

##__________________________________________________________________||
class hbheAnalyzerDummy(Analyzer):
    def process(self, event):
        event.hbheMaxZeros = 0
        event.hbheMaxHPDHits = 0
        event.hbheMaxHPDNoOtherHits = 0
        event.hbheHasBadRBXTS4TS5 = 0
        event.hbheGoodJetFoundInLowBVRegion = 1
        event.hbheHasBadRBXRechitR45Loose = 0
        event.hbheFilterNew = 1
        event.hbheFilterNewTight = 1
        event.hbheFilterIso = 1

##__________________________________________________________________||
