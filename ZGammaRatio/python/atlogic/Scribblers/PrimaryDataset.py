# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class PrimaryDataset(object):
    def begin(self, event):
        self.vals = [ ]
        event.PrimaryDataset = self.vals

        # assume the first string before '_' is the primary dataset name
        # e.g., 'HTMHT' if "HTMHT_Run2015D_PromptReco_25ns"
        pd = event.componentName[0].split('_')[0]
        self.vals[:] = [pd]

    def event(self, event):
        event.PrimaryDataset = self.vals

##__________________________________________________________________||
