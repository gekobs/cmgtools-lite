
##__________________________________________________________________||
class EventSelectionAny(object):
    """select events that meet any of the conditions

    """

    def __init__(self, name = None):
        if name is not None: self.name = name
        self.selections = [ ]

    def add(self, selection):
        self.selections.append(selection)

    def begin(self, event):
        for s in self.selections:
            if hasattr(s, 'begin'): s.begin(event)

    def event(self, event):
        for s in self.selections:
            if s(event): return True
        return False

    def __call__(self, event):
        return self.event(event)

    def end(self):
        for s in self.selections:
            if hasattr(s, 'end'): s.end()

##__________________________________________________________________||
