# Tai Sakuma <tai.sakuma@cern.ch>
from .determin_bintypeId import bintype_name_dict

##__________________________________________________________________||
class bintype(object):
    def begin(self, event):
        self.addr_bintype = [ ]
        event.bintype = self.addr_bintype

    def event(self, event):
        event.bintype = self.addr_bintype
        self.addr_bintype[:] = [bintype_name_dict[event.bintypeId[0]]]

##__________________________________________________________________||
