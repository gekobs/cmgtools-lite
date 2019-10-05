from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event

##__________________________________________________________________||
class AtScribblerRunner(Analyzer):
    def beginLoop(self, setup):
        super(AtScribblerRunner, self).beginLoop(setup)
        self.scribblers = self.cfg_ana.scribblers
        self.first = True

    def process(self, event):
        self.readCollections( event.input )
        if self.first:
            for s in self.scribblers: s.begin(event)
            self.first = False
        for s in self.scribblers: s.event(event)

##__________________________________________________________________||
