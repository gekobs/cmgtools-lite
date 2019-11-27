import os
import PhysicsTools.HeppyCore.framework.config as cfg

##__________________________________________________________________||
import logging
# levels: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logging.basicConfig( level = logging.WARNING )

##__________________________________________________________________||
import CMGTools.ZGammaRatio.components.components_Data_2016 as cmps

componentList =  [ ]

# 94X Legacy re-miniAOD

# componentList.extend(cmps.componentList_Run2016B_17Jul2018_v1)
# componentList.extend(cmps.componentList_Run2016B_17Jul2018_v2)
# componentList.extend(cmps.componentList_Run2016C_17Jul2018_v1)
# componentList.extend(cmps.componentList_Run2016D_17Jul2018_v1)
# componentList.extend(cmps.componentList_Run2016E_17Jul2018_v1)
# componentList.extend(cmps.componentList_Run2016F_17Jul2018_v1)
# componentList.extend(cmps.componentList_Run2016G_17Jul2018_v1)
# componentList.extend(cmps.componentList_Run2016H_17Jul2018_v1)

componentList.append(cmps.SinglePhoton_Run2016B_17Jul2018_v1)
componentList.append(cmps.SinglePhoton_Run2016B_17Jul2018_v2)
componentList.append(cmps.SinglePhoton_Run2016C_17Jul2018_v1)
componentList.append(cmps.SinglePhoton_Run2016D_17Jul2018_v1)
componentList.append(cmps.SinglePhoton_Run2016E_17Jul2018_v1)
componentList.append(cmps.SinglePhoton_Run2016F_17Jul2018_v1)
componentList.append(cmps.SinglePhoton_Run2016G_17Jul2018_v1)
componentList.append(cmps.SinglePhoton_Run2016H_17Jul2018_v1)

##__________________________________________________________________||
from CMGTools.ZGammaRatio.components.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

components = [kreator.makeDataComponent(**s) for s in componentList]
for comp in components:
    # comp.files[:] = comp.files[1:3] # for batch submission test
    comp.splitFactor = len(comp.files)

##__________________________________________________________________||
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
test = getHeppyOption('test')
if test == "1" :
    componentList = [cmps.SinglePhoton_Run2016H_17Jul2018_v1]
    components = [kreator.makeDataComponent(**s) for s in componentList]
    for comp in components:
        comp.files[:] = comp.files[15:16]
        print comp.files
        comp.splitFactor = len(comp.files)
elif test == "2" : #heavy test
    components = [kreator.makeDataComponent(**s) for s in componentList]
    for comp in components:
        comp.files = comp.files[0:3]
        print comp.files
        comp.splitFactor = len(comp.files)

##__________________________________________________________________||
datamc = 'data'
runPreProcessor = False

##__________________________________________________________________||
from CMGTools.ZGammaRatio.buildSequence import buildSequence
from CMGTools.ZGammaRatio.atlogic.eventSelectionPathCfgDicts import event_selection_path_cfg_tree_production

scribbler_options = dict(datamc = datamc, pd = True, gen_process = False)
buildEventSelection_options = dict(path_cfg = event_selection_path_cfg_tree_production)

sequence = buildSequence(
    datamc,
    scribbler_options, buildEventSelection_options,
    runPreProcessor = runPreProcessor,
    )
sequence = cfg.Sequence(sequence)

##__________________________________________________________________||
if runPreProcessor:
    from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
    preprocessorFile = "$CMSSW_BASE/src/CMGTools/ZGammaRatio/python/preprocessorConfigs/cmsRun_Data_cfg.py"
    preprocessor = CmsswPreprocessor(preprocessorFile)
else:
    preprocessor = None

##__________________________________________________________________||
# the following is declared in case this cfg is used in input to the
# heppy.py script

from CMGTools.ZGammaRatio.framework.AtEvents import AtEvents
config = cfg.Config(
    components = components,
    sequence = sequence,
    preprocessor = preprocessor,
    services = [],
    events_class = AtEvents,
    )

##__________________________________________________________________||
