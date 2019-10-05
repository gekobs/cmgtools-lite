from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
import PhysicsTools.HeppyCore.framework.config as cfg
from math import *
from DataFormats.FWLite import Events, Handle

class AtLheBoson(Analyzer):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(AtLheBoson,self).__init__(cfg_ana,cfg_comp,looperName)
        self.lheh = Handle('LHEEventProduct')

    def declareHandles(self):
        super(AtLheBoson, self).declareHandles()

    def beginLoop(self, setup):
        super(AtLheBoson,self).beginLoop(setup)

    def process(self, event):

        if not self.cfg_comp.isMC: 
            return True
        
        event.lheV_pt = -1

        try:
          event.input.getByLabel('externalLHEProducer', self.lheh)
        except:            
            return True

        if not self.lheh.isValid(): return True

        self.readCollections(event.input)
        hepeup = self.lheh.product().hepeup()
        pup = hepeup.PUP
        l = None
        lBar = None
        nu = None
        nuBar = None 

        for i in xrange(len(pup)):
          id = hepeup.IDUP[i]
          status = hepeup.ISTUP[i]
          idabs = abs(id)

          if idabs in [12,14,16]:
              if id > 0:
                nu = i
              else:
                nuBar = i
          if idabs in [11,13,15]:
              if id > 0:
                l = i
              else:
                lBar = i

          v = None
          if l and lBar: # Z to LL
              v = (l,lBar)
          elif l and nuBar: # W 
              v = (l,nuBar)
          elif lBar and nu: # W 
              v = (nu,lBar)
          elif nu and nuBar: # Z to nn 
              v = (nu,nuBar)

          # Sometimes boson not found
          if v and event.lheV_pt < 0:
            event.lheV_pt = sqrt((pup[v[0]][0]+pup[v[1]][0])**2 + (pup[v[0]][1]+pup[v[1]][1])**2)

          if idabs in (22,23,24) and event.lheV_pt < 0:
              event.lheV_pt = sqrt(pup[i][0]**2 + pup[i][1]**2)

        return True

