from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters

##__________________________________________________________________||
class AtSimpleCounter(Analyzer):
    def beginLoop(self,setup):
        super(AtSimpleCounter, self).beginLoop(setup)
        self.counters.addCounter('events')
        self.max = self.cfg_ana.max
        count = self.counters.counter('events')
        for i in range(self.cfg_ana.max + 1):
            count.register(str(i))

    def process(self, event):
        self.readCollections(event.input)
        n = self.cfg_ana.func(event)
        if not n <= self.cfg_ana.max: return
        self.counters.counter('events').inc(str(n))

##__________________________________________________________________||
