from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator, testSamples
from CMGTools.Production.dataset import createDataset

##__________________________________________________________________||
def getFilesLFN(self, dataset, user, pattern, useAAA = False, run_range = None, json = None):
    ds = createDataset(user, dataset, pattern, readcache = True, run_range = run_range, json = json)
    files = ds.listOfGoodFiles()
    return files

##__________________________________________________________________||
from types import MethodType
ComponentCreator.getFiles = MethodType(getFilesLFN, None, ComponentCreator)

##__________________________________________________________________||
