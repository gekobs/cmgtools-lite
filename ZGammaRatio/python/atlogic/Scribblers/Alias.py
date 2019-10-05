# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class Alias(object):
    def __init__(self, src, alias):
        self.src = src
        self.alias = alias

    def begin(self, event):
        setattr(event, self.alias, getattr(event, self.src))

    def event(self, event):
        setattr(event, self.alias, getattr(event, self.src))

##__________________________________________________________________||
