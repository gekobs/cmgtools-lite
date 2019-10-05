import subprocess
import os
import ROOT

##__________________________________________________________________||
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
class AtEvents(Events):
    """A wrapper class of Events

    This class can receive files as LFN, i.e., starting with '/store/'

    It uses local files if they exisit. Otherwiser use AAA.

    """
    def __init__(self, files, tree_name, options = None):
        files = [self.convert_LFN_to_PFN_or_AAA(f) for f in files]
	if options is not None:
            if hasattr(options, "secondaryInputFiles"):
                options.secondaryInputFiles = [self.convert_LFN_to_PFN_or_AAA(f) for f in options.secondaryInputFiles]
        super(AtEvents, self).__init__(files, tree_name, options)

    def convert_LFN_to_PFN_or_AAA(self, path):
        if not path.startswith('/store/'): return path

        pfn = subprocess.check_output(['edmFileUtil', '-d', path]).strip()
        print 'trying to open local file: ', pfn
        f = ROOT.TFile.Open(pfn)
        if not IsROOTNullPointer(f) and f.IsOpen():
            print '  successfully opened. will use the local file'
            return pfn

        aaa = 'root://cms-xrd-global.cern.ch/%s' % path
        print '  unsuccessful. use AAA: ', aaa
        return aaa

##__________________________________________________________________||
def IsROOTNullPointer(tobject):
    try:
        tobject.GetName()
        return False
    except ReferenceError:
        return True

##__________________________________________________________________||
