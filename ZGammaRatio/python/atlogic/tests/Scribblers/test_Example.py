# Tai Sakuma <tai.sakuma@cern.ch>
from ...Scribblers.Example import Example
import unittest

##__________________________________________________________________||
class MockEvent(object):
    pass

##__________________________________________________________________||
class Test_Example(unittest.TestCase):

    def test_read_branch_address_with_same_event_object(self):
        obj = Example()
        event = MockEvent()

        obj.begin(event)
        val = event.val

        obj.event(event)
        self.assertEqual(1, val[0])

        obj.event(event)
        self.assertEqual(2, val[0])

    def test_read_event_attribute_with_same_event_object(self):
        obj = Example()
        event = MockEvent()

        obj.begin(event)

        obj.event(event)
        self.assertEqual(1, event.val[0])

        obj.event(event)
        self.assertEqual(2, event.val[0])

    def test_read_branch_address_with_different_event_objects(self):
        obj = Example()
        event = MockEvent()

        obj.begin(event)
        val = event.val

        event1 = MockEvent()
        obj.event(event1)
        self.assertEqual(1, val[0])

        event2 = MockEvent()
        obj.event(event2)
        self.assertEqual(2, val[0])

    def test_read_event_attribute_with_different_event_objects(self):
        obj = Example()
        event = MockEvent()

        obj.begin(event)

        event1 = MockEvent()
        obj.event(event1)
        self.assertEqual(1, event1.val[0])

        event2 = MockEvent()
        obj.event(event2)
        self.assertEqual(2, event2.val[0])

##__________________________________________________________________||
