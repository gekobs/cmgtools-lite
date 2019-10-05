from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters

##__________________________________________________________________||
class AtnVertCounter(Analyzer):
    def beginLoop(self,setup):
        super(AtnVertCounter, self).beginLoop(setup)
        self.counters.addCounter('events')
        self.max = 100
        count = self.counters.counter('events')
        for i in range(self.max):
            count.register(str(i))

    def process(self, event):
        self.readCollections(event.input)
        nvert = len(event.goodVertices)
        if not nvert < self.max: return
        self.counters.counter('events').inc(str(nvert))

##__________________________________________________________________||
