from PhysicsTools.HeppyCore.utils.deltar import deltaR
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event

##__________________________________________________________________||
class AtObjNoX( Analyzer ):
    """
    This class creates a list of objects which has no overlap with
    another list of objects.

    For example, this can be used to create a list of isolated tracks
    without muons.

    """
    def process(self, event):
        objects = getattr(event, self.cfg_ana.objects)
        Xs = [X for Xname in self.cfg_ana.X for X in getattr(event, Xname)] # Get a list from a list of lists
        R = self.cfg_ana.deltaR
        out = [o for o in objects if all([(deltaR(o, x) > R) for x in Xs])]
        setattr(event, self.cfg_ana.outName, out)

##__________________________________________________________________||
