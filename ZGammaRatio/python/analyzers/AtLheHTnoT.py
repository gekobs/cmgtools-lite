from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from DataFormats.FWLite import Handle

import math

##__________________________________________________________________||
class AtLheHTnoT(Analyzer):
    """
    Attach `lheHTnoT` to the `event`.

    `lheHTnoT` is the sum of the pT of the quarks and gluons, in LHE
    event record, whose status is 1 and whose ancestors don't include
     a top quark.

    The value of `lheHTnoT` is supposed to be very close to the value
    used to define the bin in the HT binned TTJets samples.

    """
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(AtLheHTnoT, self).__init__(cfg_ana, cfg_comp, looperName)
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

        ht = 0.0
        htnoT = 0.0
        htForTopQuarks = 0.0

        hepeup = self.lheh.product().hepeup()
        pup = hepeup.PUP

        for i in xrange(0, len(pup)):
          pdgabs = abs(hepeup.IDUP[i])
          status = hepeup.ISTUP[i]
          if status == 1 and (pdgabs == 21  or 1 <= pdgabs <= 6): # gluons and quarks
              pt = math.sqrt(pup[i][0]**2 + pup[i][1]**2)
              ht += pt
              if not self.isfromTopQuark(i, hepeup):
                  htnoT += pt
        event.lheHTnoT = htnoT
        return True

    def isfromTopQuark(self, index, hepeup):
        if index < 0: return False
        pdgabs = abs(hepeup.IDUP[index])
        if pdgabs == 6: return True
        firstMotherIndex = hepeup.MOTHUP[index][0] - 1 # subtact one because index
        lastMotherIndex = hepeup.MOTHUP[index][1] - 1  # starts from 1 in LHE
        return any([self.isfromTopQuark(i, hepeup) for i in range(firstMotherIndex, lastMotherIndex + 1)])

    def _attach_dummy_to(self, event):
        event.lheHTnoT = 0.0

##__________________________________________________________________||
