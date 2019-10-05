from ...Scribblers.WeightFromTbl import WeightFromTbl
import unittest

import cStringIO

##__________________________________________________________________||
input_weight_txt = """ var1  var2  var3
   2.4   1.1    0
   3.1   1.8    2
   1.8   2.1    4
"""

##__________________________________________________________________||
class MockEvent(object):
    pass

##__________________________________________________________________||
class Test_WeightFromTbl(unittest.TestCase):

    def test_event(self):
        f = cStringIO.StringIO(input_weight_txt)
        obj = WeightFromTbl(
            f,
            columnVar = 'var3', columnWeight = 'var1',
            branchVar = 'branchA', branchWeight = 'branchB'
        )

        event = MockEvent()
        obj.begin(event)

        branchB = event.branchB

        event.branchA = [0]
        obj.event(event)

        self.assertIs(branchB, event.branchB)
        self.assertEqual([2.4], branchB)

        event.branchA = [3]
        obj.event(event)
        self.assertIs(branchB, event.branchB)
        self.assertEqual([3.1], branchB)

        # give a different event object
        event1 = MockEvent()
        event1.branchA = [4]
        obj.event(event1)
        self.assertIs(branchB, event1.branchB)
        self.assertEqual([1.8], branchB)

##__________________________________________________________________||
