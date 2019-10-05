#!/usr/bin/env python
from Scribblers.Alias import Alias
from Scribblers.PrimaryDataset import PrimaryDataset
from Scribblers.inCertifiedLumiSections import inCertifiedLumiSections
from Scribblers.cutflowId import cutflowId
from Scribblers.cutflow import cutflow
from Scribblers.metNoX import metNoX
from Scribblers.WeightFromTbl import WeightFromTbl
from Scribblers.componentName import componentName
from Scribblers.GenProcess import GenProcess
from Scribblers.njetnbjetbin import njetnbjetbin
from Scribblers.htbin import htbin
from Scribblers.bintypeId import bintypeId
from Scribblers.bintypeIdJECUp import bintypeIdJECUp
from Scribblers.bintypeIdJECDown import bintypeIdJECDown
from Scribblers.bintype import bintype
from Scribblers.bintypeJECUp import bintypeJECUp
from Scribblers.bintypeJECDown import bintypeJECDown
from Scribblers.metNoXNoHF import metNoXNoHF
from Scribblers.MhtOverMet import MhtOverMet
from Scribblers.MhtOverMetNoHF import MhtOverMetNoHF
from Scribblers.MhtOverMetNoX import MhtOverMetNoX
from Scribblers.MhtOverMetNoXNoHF import MhtOverMetNoXNoHF
from Scribblers.nMuonsIsolated import nMuonsIsolated
from Scribblers.nElectronsIsolated import nElectronsIsolated
from Scribblers.nElectronsBarrel import nElectronsBarrel
from Scribblers.nPhotons200 import nPhotons200
from Scribblers.inEventList import inEventList

import os

##__________________________________________________________________||
def buildScribblerPathForLoopingOverTrees_preEventSelection(
        datamc,
        json = None,
        tbl_pu_corr_path = None,
        met_filter_event_lists_dir = None,
        metnohf = False):
    """
    Args:

    datamc: "data" or "mc"

    json: path to json file for certified data

    tbl_pu_corr_path: path to table with pileup reweighing factors

    met_filter_event_lists_dir: path to dir with bad event list text files

    metnohf: True or False

    """

    ret = [ ]

    ret.append(componentName())


    if datamc == 'data':
        ret.append(PrimaryDataset())

    if datamc == 'mc':
        ret.append(GenProcess())

    if datamc == 'data' and json is not None:
        ret.append(inCertifiedLumiSections(json))

    if datamc == 'data' and met_filter_event_lists_dir is not None:
        bad_event_list_files = (
            'badResolutionTrack_Jan13.txt',
            'csc2015_Dec01.txt',
            'ecalscn1043093_Dec01.txt',
            'muonBadTrack_Jan13.txt',
        )
        bad_event_list_paths = [os.path.join(met_filter_event_lists_dir, f) for f in bad_event_list_files]
        ret.append(inEventList(bad_event_list_paths, 'inBadEventList'))

    # ret.append(cutflowId())
    # ret.append(bintypeId())
    # ret.append(bintypeIdJECUp())
    # ret.append(bintypeIdJECDown())

    ret.append(htbin())
    ret.append(metNoX())
    ret.append(MhtOverMet())
    ret.append(MhtOverMetNoX())

    ret.append(nMuonsIsolated())
    ret.append(nElectronsIsolated())
    ret.append(nElectronsBarrel())
    ret.append(nPhotons200())

    if metnohf:
        ret.append(metNoXNoHF())
        ret.append(MhtOverMetNoHF())
        ret.append(MhtOverMetNoXNoHF())

    return ret

##__________________________________________________________________||
def buildScribblerPathForLoopingOverTrees_postEventSelection(
        datamc,
        json = None,
        tbl_pu_corr_path = None,
        met_filter_event_lists_dir = None,
        metnohf = False):
    """
    Args:

    datamc: "data" or "mc"

    json: path to json file for certified data

    tbl_pu_corr_path: path to table with pileup reweighing factors

    met_filter_event_lists_dir: path to dir with bad event list text files

    metnohf: True or False

    """

    ret = [ ]

    if datamc == 'mc' and tbl_pu_corr_path is not None:
        ret.append(
            WeightFromTbl(
                tbl_pu_corr_path,
                columnVar = 'nTrueInt', columnWeight = 'corr',
                branchVar = 'nTrueInt', branchWeight = 'puWeightFromTbl'
            )
        )

    ret.append(cutflow())

    ret.append(njetnbjetbin())
    ret.append(bintype())
    ret.append(bintypeJECUp())
    ret.append(bintypeJECDown())

    return ret

##__________________________________________________________________||
