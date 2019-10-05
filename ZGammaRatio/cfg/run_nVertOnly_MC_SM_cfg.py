import os
import PhysicsTools.HeppyCore.framework.config as cfg

##__________________________________________________________________||
import logging
# levels: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logging.basicConfig( level = logging.WARNING )

##__________________________________________________________________||
import CMGTools.TTHAnalysis.components.components_alphaT_13TeV_MC_74X as cmps
componentArgsList = [ ]
componentArgsList.extend(cmps.componentArgsList_NeutrinoGuns_25ns)
componentArgsList.extend([cmps.QCD_Pt80to120_25ns])

##__________________________________________________________________||
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

hostname = os.environ["HOSTNAME"]
if 'hep.ph.ic.ac.uk' in hostname:
    ## kreator.getFiles = kreator.getFilesFromIC
    kreator.getFiles = kreator.getFilesLFN

if 'dice.priv' in hostname or 'soolin.phy.bris.ac.uk' in hostname:
    ## kreator.getFiles = kreator.getFilesFromBristol
    ## kreator.getFiles = kreator.getFilesPFNifExistOrAAA
    kreator.getFiles = kreator.getFilesLFN

##__________________________________________________________________||
components = [kreator.makeMCComponent(**s) for s in componentArgsList]
for comp in components:
    comp.splitFactor = len(comp.files)

##__________________________________________________________________||
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
test = getHeppyOption('test')
if test == "1" :
    componentArgsList = [cmps.QCD_Pt80to120_25ns]
    components = [kreator.makeMCComponent(**s) for s in componentArgsList]
    for comp in components:
        comp.files = comp.files[0:1]
        print comp.files
        comp.splitFactor = len(comp.files)

##__________________________________________________________________||
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer
vertexAna = cfg.Analyzer(
    VertexAnalyzer, name="VertexAnalyzer",
    vertexWeight = None,
    fixedWeight = 1,
    keepFailingEvents = True,
    verbose = False
    )

from CMGTools.TTHAnalysis.analyzers.AtSimpleCounter import AtSimpleCounter
atnVertCounter =  cfg.Analyzer(
    AtSimpleCounter, name="AtnVertCounter",
    max = 100,
    func = lambda ev: len(ev.goodVertices)
    )

from PhysicsTools.Heppy.analyzers.core.PileUpAnalyzer import PileUpAnalyzer
pileUpAna = cfg.Analyzer(
    PileUpAnalyzer, name="PileUpAnalyzer",
    true = True,
    makeHists = True
    )

sequence = cfg.Sequence([vertexAna, atnVertCounter, pileUpAna])

##__________________________________________________________________||
# the following is declared in case this cfg is used in input to the
# heppy.py script

from CMGTools.TTHAnalysis.framework.AtEvents import AtEvents
config = cfg.Config(components = components,
                    sequence = sequence,
                    preprocessor = None,
                    services = [],
                    events_class = AtEvents)

##__________________________________________________________________||
