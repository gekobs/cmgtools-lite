# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class inEventList(object):
    def __init__(self, event_list_paths, branch_name):
        self.branch_name = branch_name
        self.event_list_paths = event_list_paths

        self.eventList = set()
        for path in self.event_list_paths:
            self.eventList.update({l.strip() for l in open(path)})

    def begin(self, event):
        self.vals = [ ]
        setattr(event, self.branch_name, self.vals)

    def event(self, event):
        setattr(event, self.branch_name, self.vals)

        evId = "{}:{}:{}".format(event.run[0], event.lumi[0], event.evt[0])
        # e.g., 260627:1708:3096828758

        self.vals[:] = [evId in self.eventList]

    def end(self):
        self.eventList = None

##__________________________________________________________________||
