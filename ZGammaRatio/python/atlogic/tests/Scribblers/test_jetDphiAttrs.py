from ...Scribblers.jetDphiAttrs import jetDphiAttrs
import unittest
import numpy as np

##__________________________________________________________________||
class MockEvent(object):
    pass

##__________________________________________________________________||
class Test_jetDphiAttrs(unittest.TestCase):

    def test__monojet(self):
        obj = jetDphiAttrs(
            inJetPrefix = 'jet',
            outJetPrefix = 'jet40',
            minJetPt = 40
        )

        event = MockEvent()
        obj.begin(event)

        event.jet_pt = [40.2]
        event.jet_phi = [0.2]
        obj.event(event)

        self.assertEqual([1.0], event.jet40_f)
        self.assertEqual([-1.0], event.jet40_g)
        self.assertEqual([0.0], event.jet40_k)
        self.assertEqual([np.pi], event.jet40_dphi)
        self.assertEqual([np.pi/2], event.jet40_bDphi)
        self.assertEqual([np.pi/2], event.jet40_chi)


##__________________________________________________________________||
