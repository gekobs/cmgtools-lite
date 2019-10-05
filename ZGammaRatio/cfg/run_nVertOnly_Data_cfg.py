import os
import PhysicsTools.HeppyCore.framework.config as cfg

##__________________________________________________________________||
import logging
# levels: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logging.basicConfig( level = logging.WARNING )

##__________________________________________________________________||
import CMGTools.TTHAnalysis.components.components_alphaT_13TeV_DATA_2015 as cmps
# componentArgsList = [cmps.zeroBias_Run2015D_05Oct2015_v1_DCSONLY, cmps.zeroBias_Run2015D_PromptReco_v4_DCSONLY]
componentArgsList = [cmps.zeroBias_Run2015D_05Oct2015_v1_Cert_25ns, cmps.zeroBias_Run2015D_PromptReco_v4_Cert_25ns]

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
components = [kreator.makeDataComponent(**s) for s in componentArgsList]
for comp in components:
    comp.splitFactor = len(comp.files)

##__________________________________________________________________||
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
test = getHeppyOption('test')
if test == "1" :
    componentArgsList = [cmps.zeroBias_Run2015D_PromptReco_v4_DCSONLY]
    components = [kreator.makeDataComponent(**s) for s in componentArgsList]
    for comp in components:
        comp.files = comp.files[5:6]
        print comp.files
        comp.splitFactor = len(comp.files)

##__________________________________________________________________||
from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer import JSONAnalyzer
jsonAna = cfg.Analyzer(
    JSONAnalyzer, name="JSONAnalyzer",
    )

from PhysicsTools.Heppy.analyzers.core.TriggerBitFilter import TriggerBitFilter
triggerBitFilter = cfg.Analyzer(
    TriggerBitFilter, name="TriggerBitFilter",
    )

from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer
vertexAna = cfg.Analyzer(
    VertexAnalyzer, name="VertexAnalyzer",
    vertexWeight = None,
    fixedWeight = 1,
    keepFailingEvents = True,
    verbose = False
    )

from CMGTools.TTHAnalysis.analyzers.AtnVertCounter import AtnVertCounter
atnVertCounter =  cfg.Analyzer(
    AtnVertCounter, name="AtnVertCounter",
    )

sequence = cfg.Sequence([jsonAna, triggerBitFilter, vertexAna, atnVertCounter])

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
