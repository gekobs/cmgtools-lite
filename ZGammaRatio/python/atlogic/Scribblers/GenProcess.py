# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class GenProcess(object):
    def begin(self, event):
        self.vals = [ ]
        event.GenProcess = self.vals

        # assume the first string before '_' is the name of the generated process
        # e.g., 'QCD' if "QCD_HT1500to2000_25ns"
        pd = event.componentName[0].split('_')[0]
        self.vals[:] = [pd]

    def event(self, event):
        event.GenProcess = self.vals

##__________________________________________________________________||
