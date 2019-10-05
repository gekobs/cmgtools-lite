from PhysicsTools.HeppyCore.utils.deltar import deltaR
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
import copy

##__________________________________________________________________||
class AtJetsJECVariations(Analyzer):
    def process(self, event):
        self.readCollections(event.input)

        jets = getattr(event, self.cfg_ana.jets_in)

        jets_up = [copy.copy(j) for j in jets]
        for j in jets_up: j.setP4(j.p4()/j.corr*j.corrJECUp)
        jets_up.sort(key = lambda j : j.pt(), reverse = True)
        setattr(event, self.cfg_ana.jets_out_up, jets_up)

        jets_down = [copy.copy(j) for j in jets]
        for j in jets_down: j.setP4(j.p4()/j.corr*j.corrJECDown)
        jets_down.sort(key = lambda j : j.pt(), reverse = True)
        setattr(event, self.cfg_ana.jets_out_down, jets_down)

##__________________________________________________________________||
