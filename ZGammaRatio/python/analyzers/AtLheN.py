from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from DataFormats.FWLite import Handle

import math

##__________________________________________________________________||
class AtLheN(Analyzer):
    """
    Attach `nLheElectrons`, `nLheMuos`, `nLheTaus` to the `event`.

    These are the numbers of the electrons, muons, and taus in LHE.

    """
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(AtLheN, self).__init__(cfg_ana, cfg_comp, looperName)
        self.lheh = Handle('LHEEventProduct')

    def process(self, event):
        if not self.cfg_comp.isMC: return True

        try:
          event.input.getByLabel('externalLHEProducer', self.lheh)
        except :
            self._attach_dummy_to(event)
            return True

        if not self.lheh.isValid() :
            self._attach_dummy_to(event)
            return True

        self.readCollections( event.input )

        nLheElectrons = 0
        nLheMuons = 0
        nLheTaus = 0

        hepeup = self.lheh.product().hepeup()
        pup = hepeup.PUP

        for i in xrange(0, len(pup)):
          pdgabs = abs(hepeup.IDUP[i])
          status = hepeup.ISTUP[i]
          if status == 1 and pdgabs == 11:
              nLheElectrons += 1
          if status == 1 and pdgabs == 13:
              nLheMuons += 1
          if status == 1 and pdgabs == 15:
              nLheTaus += 1

        event.nLheElectrons = nLheElectrons
        event.nLheMuons = nLheMuons
        event.nLheTaus = nLheTaus

        return True

    def _attach_dummy_to(self, event):
        event.nLheElectrons = 0
        event.nLheMuons = 0
        event.nLheTaus = 0


##__________________________________________________________________||
