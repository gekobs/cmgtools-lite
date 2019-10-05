from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event

##__________________________________________________________________||
class AtObjSelectionFunc( Analyzer ):
    """
    This class creates a list of objects selected from another list by
    the given function.

    """
    def process(self, event):
        objects = getattr(event, self.cfg_ana.objects)
        out = [o for o in objects if self.cfg_ana.func(o)]
        setattr(event, self.cfg_ana.outName, out)

##__________________________________________________________________||
