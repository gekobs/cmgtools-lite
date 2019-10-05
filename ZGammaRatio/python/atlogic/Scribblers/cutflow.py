# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class cutflow(object):
    def begin(self, event):
        self.addr_cutflow = [ ]
        event.cutflow = self.addr_cutflow

        self.cutflow_name_dict = {
            1 : 'Signal', 2 : 'SingleMu', 3 : 'DoubleMu',
            4 : 'SingleEle', 5 : 'DoubleEle', 6 : 'SinglePhoton',
            7 : 'SingleMuEle',
            -1 : 'other'
            }

    def event(self, event):
        event.cutflow = self.addr_cutflow
        self.addr_cutflow[:] = [self.cutflow_name_dict[event.cutflowId[0]]]

##__________________________________________________________________||
