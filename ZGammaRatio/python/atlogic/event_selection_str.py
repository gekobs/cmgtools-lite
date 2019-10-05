from .EventSelectionModules.EventSelectionAll import EventSelectionAll
from .EventSelectionModules.EventSelectionAny import EventSelectionAny
from .EventSelectionModules.EventSelectionNot import EventSelectionNot
from .EventSelectionModules.LambdaStr import LambdaStr

##__________________________________________________________________||
def event_selection_str(eventSelection):
    out = event_selection_io(eventSelection)
    return out.getvalue()

##__________________________________________________________________||
def event_selection_io(eventSelection, out = None, prep = ''):

    if out is None:
        import StringIO
        out = StringIO.StringIO()

    import inspect

    def print_name(es):
        ret = '<'
        if hasattr(es, 'name'):
            ret += str(es.name)
        ret += (':')
        if inspect.isfunction(es):
            ret += es.__name__
        else:
            ret += es.__class__.__name__
        ret += '>'
        return ret

    out.write(prep)

    if hasattr(eventSelection, 'lambda_str'):
        out.write(print_name(eventSelection))
        out.write(' ')
        out.write(eventSelection.lambda_str)
        out.write('\n')
        return out

    if isinstance(eventSelection, EventSelectionAll):
        out.write(print_name(eventSelection))
        out.write('\n')
        for e in eventSelection.selections:
            event_selection_io(e, out, prep + '  ')
        return out

    if isinstance(eventSelection, EventSelectionAny):
        out.write(print_name(eventSelection))
        out.write('\n')
        for e in eventSelection.selections:
            event_selection_io(e, out, prep + '  ')
        return out

    if isinstance(eventSelection, EventSelectionNot):
        out.write(print_name(eventSelection))
        out.write('\n')
        event_selection_io(eventSelection.selection, out, prep + '  ')
        return out

    out.write(print_name(eventSelection))
    out.write('\n')

    return out


##__________________________________________________________________||
