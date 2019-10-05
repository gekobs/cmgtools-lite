# Tai Sakuma <tai.sakuma@cern.ch>
from .determin_bintypeId import bintype_name_dict

##__________________________________________________________________||
class bintypeJECUp(object):
    def begin(self, event):
        self.addr_bintype = [ ]
        event.bintypeJECUp = self.addr_bintype

    def event(self, event):
        event.bintypeJECUp = self.addr_bintype
        self.addr_bintype[:] = [bintype_name_dict[event.bintypeIdJECUp[0]]]

##__________________________________________________________________||
