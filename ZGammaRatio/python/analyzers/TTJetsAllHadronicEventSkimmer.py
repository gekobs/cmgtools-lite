from math import *
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
import os
        
class TTJetsAllHadronicEventSkimmer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(TTJetsAllHadronicEventSkimmer,self).__init__(cfg_ana,cfg_comp,looperName)


    def declareHandles(self):
        super(TTJetsAllHadronicEventSkimmer, self).declareHandles()


    def beginLoop(self, setup):
        super(TTJetsAllHadronicEventSkimmer,self).beginLoop(setup)
        self.counters.addCounter('events')
        self.count = self.counters.counter('events')
        self.count.register('all events')
        self.count.register('passing events')

        

    def process(self, event):
        self.readCollections( event.input )
        self.count.inc('all events')

        if event.nLheMuons > 0 or event.nLheElectrons > 0 or event.nLheTaus > 0: return False
                                    
        self.count.inc('passing events')
        return True    
