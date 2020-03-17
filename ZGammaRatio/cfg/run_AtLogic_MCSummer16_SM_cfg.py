import os
import PhysicsTools.HeppyCore.framework.config as cfg

##__________________________________________________________________||
import logging
# levels: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logging.basicConfig( level = logging.WARNING )

##__________________________________________________________________||
import CMGTools.ZGammaRatio.components.components_MC_SM_Summer16 as cmps

componentList = []

# componentList.extend(cmps.componentList_TTJets)
# componentList.extend(cmps.componentList_SingleTop)
# componentList.extend(cmps.componentList_WJets)
componentList.extend(cmps.componentList_DYJets)
# componentList.extend(cmps.componentList_DYJets_NJ)
componentList.extend(cmps.componentList_GJets)
componentList.extend(cmps.componentList_DYJets_sherpa)
componentList.extend(cmps.componentList_G1Jet)
# componentList.extend(cmps.componentList_VGamma)
# componentList.extend(cmps.componentList_QCD)
# componentList.extend(cmps.componentList_DiBoson)
# componentList.extend(cmps.componentList_TTX)
# componentList.extend(cmps.componentList_EWKV2Jets)

##__________________________________________________________________||
from CMGTools.ZGammaRatio.components.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
test = getHeppyOption('test')
if test == "1" : #lite test
    componentList = [cmps.DYJetsToee_Pt0toInf_sherpa]
    components = [kreator.makeMCComponent(**s) for s in componentList]
    for comp in components:
        comp.files = comp.files[0:1]
        print comp.files
        comp.splitFactor = len(comp.files)
elif test == "2" : #heavy test
    components = [kreator.makeMCComponent(**s) for s in componentList]
    for comp in components:
        comp.files = comp.files[0:3]
        print comp.files
        comp.splitFactor = len(comp.files)
else: # for production
    components = [kreator.makeMCComponent(**s) for s in componentList]
    for comp in components:
        # comp.files = comp.files[1:3] # for batch submission test
        comp.splitFactor = min(len(comp.files),1000)

##__________________________________________________________________||
datamc = 'mc'
runPreProcessor = False

##__________________________________________________________________||
from CMGTools.ZGammaRatio.buildSequence import buildSequence
from CMGTools.ZGammaRatio.atlogic.eventSelectionPathCfgDicts import event_selection_path_cfg_tree_production

scribbler_options = dict(datamc = datamc, pd = False, gen_process = False)
buildEventSelection_options = dict(path_cfg = event_selection_path_cfg_tree_production)

sequence = buildSequence(
    datamc,
    scribbler_options,
    buildEventSelection_options,
    runPreProcessor = runPreProcessor,
    )
sequence = cfg.Sequence(sequence)

##__________________________________________________________________||
if runPreProcessor:
    from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
    preprocessorFile = "$CMSSW_BASE/src/CMGTools/ZGammaRatio/python/preprocessorConfigs/cmsRun_MC_cfg_.py"
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
