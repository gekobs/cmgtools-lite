# Tai Sakuma <tai.sakuma@cern.ch>

##__________________________________________________________________||
class LambdaStr(object):
    """select events to which a lambda returns True.

    A lambda should be given as a string to __init__ and will be
    evaluated in begin(). This is because a lambda is not picklable.

    In the multiprocessing mode, __init__() is called in the main
    process. Then, the instance will be pickled and sent to
    subprocesses. begin() will be called in the subprocesses.

    """
    def __init__(self, lambda_str, name = None):
        if name is not None: self.name = name
        self.lambda_str = lambda_str

    def begin(self, event):
        self.func = eval('lambda ' + self.lambda_str)

    def event(self, event):
        try:
            return self.func(event)
        except BaseException as e:
            raise ValueError('{}: error in executing "{}". raised -- {}: {}'.format(
                self.__class__.__name__,
                self.lambda_str, type(e).__name__, e
            ))

    def __call__(self, event):
        return self.event(event)

    def end(self):
        self.func = None

##__________________________________________________________________||
