# Tai Sakuma <tai.sakuma@cern.ch>
import ast
from operator import itemgetter
from ..Binning import Binning

##__________________________________________________________________||
class WeightFromTbl(object):
    """
    Args:
        path (str or file): the file or path of the input table file
        columnVar (str): the column name for the key in the input table
        columnWeight (str): the column name for the weight in the input table
        branchVar (str): the branch name for the key to read in the event
        branchWeight (str): the branch name for the weight to attach to the event
    """
    def __init__(self, path, columnVar, columnWeight, branchVar, branchWeight):
        try:
            with open(path) as f:
                self._read_file(f, columnVar, columnWeight)
        except TypeError:
            self._read_file(path, columnVar, columnWeight)

        self.branchVar = branchVar
        self.branchWeight = branchWeight

    def _read_file(self, f, columnVar, columnWeight):

        columns = f.readline().split()
        # e.g. ['nVert', 'corr', 'corr_up', 'corr_down']

        self.varName = columns[0]
        # e.g. 'nVert'

        indices = [columns.index(n) for n in (columnVar, columnWeight)]
        # [0, 1] if (columnVar, columnWeight) = ('nVert', 'corr')

        igetter = itemgetter(*indices)

        self.weightDict = dict([[ast.literal_eval(e) for e in igetter(l.split())] for l in f])
        # e.g.,  {1: 18.59651, 2: 5.441605, 3: 3.31272, 4: 2.687147, 5: 2.396046, 6: 2.246987}

        self.binning = Binning(boundaries = sorted(self.weightDict.keys()))

    def begin(self, event):
        self.vals = [ ]
        setattr(event, self.branchWeight, self.vals)

    def event(self, event):
        setattr(event, self.branchWeight, self.vals)
        self.vals[:] = [self.weightDict[self.binning(getattr(event, self.branchVar)[0])]]

##__________________________________________________________________||
