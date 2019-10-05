from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters

import pickle
import os

##__________________________________________________________________||
class AtEventSelectionRunner(Analyzer):
    def beginLoop(self, setup):
        super(AtEventSelectionRunner, self).beginLoop(setup)
        self.selection = self.cfg_ana.function
        self.first = True
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all')
        count.register('passed')

    def process(self, event):
        self.readCollections(event.input)
        if self.first:
            if hasattr(self.selection, 'begin'): self.selection.begin(event)
            self.first = False
        self.counters.counter('events').inc('all')
        if not self.selection(event): return False
        self.counters.counter('events').inc('passed')
        return True

    def write(self, setup):
        super(AtEventSelectionRunner, self).write(setup)
        from CMGTools.ZGammaRatio.atlogic.event_selection_str import event_selection_str
        string = event_selection_str(self.selection)
        string = str_ignore_add(string)
        pckfile = open(os.path.join(self.dirName, 'selection.pck'), 'w')
        pickle.dump(string, pckfile)
        pckfile.close()
        txtfile = open(os.path.join(self.dirName, 'selection.txt'), 'w')
        txtfile.write(string)
        txtfile.close()

##__________________________________________________________________||
class str_ignore_add(str):
    def __iadd__(self, other): return self
    def __add__(self, other): return self

##__________________________________________________________________||
