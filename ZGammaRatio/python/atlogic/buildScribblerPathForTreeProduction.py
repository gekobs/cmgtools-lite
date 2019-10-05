#!/usr/bin/env python
from Scribblers.Alias import Alias
from Scribblers.PrimaryDataset import PrimaryDataset
from Scribblers.inCertifiedLumiSections import inCertifiedLumiSections
from Scribblers.cutflowId import cutflowId
from Scribblers.metNoX import metNoX
from Scribblers.WeightFromTbl import WeightFromTbl
from Scribblers.componentName import componentName
from Scribblers.GenProcess import GenProcess
from Scribblers.njetnbjetbin import njetnbjetbin
from Scribblers.htbin import htbin
from Scribblers.bintypeId import bintypeId
from Scribblers.bintypeIdJECUp import bintypeIdJECUp
from Scribblers.bintypeIdJECDown import bintypeIdJECDown
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
from Scribblers.jetDphiAttrs import jetDphiAttrs
from Scribblers.minimum import minimum
from Scribblers.maximum import maximum
from Scribblers.xi import xi
from Scribblers.sin import sin
from Scribblers.tan import tan

##__________________________________________________________________||
def buildScribblerPathForTreeProduction(datamc, pd, gen_process, json = None, metnohf = False):
    """
    Args:

    datamc: "data" or "mc"

    pd: True or False

    gen_process: True or False

    json: path to json file for certified data

    metnohf: True or False

    """

    ret = [ ]
    if datamc == 'data' and pd:
        ret.append(PrimaryDataset())

    if datamc == 'mc' and gen_process:
        ret.append(GenProcess())

    if datamc == 'data' and json is not None:
        ret.append(inCertifiedLumiSections(json))

    ret.append(cutflowId())

    ret.append(bintypeId())
    ret.append(bintypeIdJECUp())
    ret.append(bintypeIdJECDown())

    ## pT >= 40
    ret.append(jetDphiAttrs(inJetPrefix = 'jet', outJetPrefix = 'jet40', minJetPt = 40))
    ret.append(minimum(srcName = 'jet40_dphi', outName = 'minDphi', default_value = -1))
    ret.append(minimum(srcName = 'jet40_bDphi', outName = 'minbDphi', default_value = -1))
    ret.append(minimum(srcName = 'jet40_dphiTilde', outName = 'minDphiTilde', default_value = -1))
    ret.append(minimum(srcName = 'jet40_omega', outName = 'minOmega', default_value = -1))
    ret.append(minimum(srcName = 'jet40_omegaHat', outName = 'minOmegaHat', default_value = -1))
    ret.append(minimum(srcName = 'jet40_omegaTilde', outName = 'minOmegaTilde', default_value = -1))
    ret.append(minimum(srcName = 'jet40_chi', outName = 'minChi', default_value = -1))
    ret.append(minimum(srcName = 'jet40_arccotF', outName = 'minArccotF', default_value = -1))
    ret.append(maximum(srcName = 'jet40_dphi', outName = 'maxDphi', default_value = -1))
    ret.append(maximum(srcName = 'jet40_f', outName = 'maxF', default_value = -1))
    ret.append(maximum(srcName = 'jet40_h', outName = 'maxH', default_value = -1))
    ret.append(xi(srcMinDphiTilde = 'minDphiTilde', srcMaxH = 'maxH', outName = 'xi'))
    ret.append(sin(srcName = 'jet40_dphiTilde', outName = 'jet40_sinDphiTilde'))
    ret.append(minimum(srcName = 'jet40_sinDphiTilde', outName = 'minSinDphiTilde', default_value = 99))
    ret.append(tan(srcName = 'jet40_chi', outName = 'jet40_tanChi'))
    ret.append(minimum(srcName = 'jet40_tanChi', outName = 'minTanChi', default_value = 99))

    ## chi with JEC variation
    ret.append(jetDphiAttrs(inJetPrefix = 'jetJECUp', outJetPrefix = 'jetJECUp40', minJetPt = 40))
    ret.append(minimum(srcName = 'jetJECUp40_chi', outName = 'minChiJECUp', default_value = -1))
    ret.append(jetDphiAttrs(inJetPrefix = 'jetJECDown', outJetPrefix = 'jetJECDown40', minJetPt = 40))
    ret.append(minimum(srcName = 'jetJECDown40_chi', outName = 'minChiJECDown', default_value = -1))

    ## with lower jet pT thresholds
    for minJetPt in (10, 15, 20):
        ret.append(jetDphiAttrs(inJetPrefix = 'jet', outJetPrefix = 'jet{}'.format(minJetPt), minJetPt = minJetPt))
        ret.append(minimum(srcName = 'jet{}_dphi'.format(minJetPt), outName = 'minDphi{}'.format(minJetPt), default_value = -1))
        ret.append(minimum(srcName = 'jet{}_bDphi'.format(minJetPt), outName = 'minbDphi{}'.format(minJetPt), default_value = -1))
        ret.append(minimum(srcName = 'jet{}_dphiTilde'.format(minJetPt), outName = 'minDphiTilde{}'.format(minJetPt), default_value = -1))
        ret.append(minimum(srcName = 'jet{}_omega'.format(minJetPt), outName = 'minOmega{}'.format(minJetPt), default_value = -1))
        ret.append(minimum(srcName = 'jet{}_omegaHat'.format(minJetPt), outName = 'minOmegaHat{}'.format(minJetPt), default_value = -1))
        ret.append(minimum(srcName = 'jet{}_omegaTilde'.format(minJetPt), outName = 'minOmegaTilde{}'.format(minJetPt), default_value = -1))
        ret.append(minimum(srcName = 'jet{}_chi'.format(minJetPt), outName = 'minChi{}'.format(minJetPt), default_value = -1))
        ret.append(minimum(srcName = 'jet{}_arccotF'.format(minJetPt), outName = 'minArccotF{}'.format(minJetPt), default_value = -1))
        ret.append(maximum(srcName = 'jet{}_dphi'.format(minJetPt), outName = 'maxDphi{}'.format(minJetPt), default_value = -1))
        ret.append(maximum(srcName = 'jet{}_f'.format(minJetPt), outName = 'maxF{}'.format(minJetPt), default_value = -1))
        ret.append(maximum(srcName = 'jet{}_h'.format(minJetPt), outName = 'maxH{}'.format(minJetPt), default_value = -1))
        ret.append(xi(srcMinDphiTilde = 'minDphiTilde{}'.format(minJetPt), srcMaxH = 'maxH{}'.format(minJetPt), outName = 'xi{}'.format(minJetPt)))
        ret.append(sin(srcName = 'jet{}_dphiTilde'.format(minJetPt), outName = 'jet{}_sinDphiTilde'.format(minJetPt)))
        ret.append(minimum(srcName = 'jet{}_sinDphiTilde'.format(minJetPt), outName = 'minSinDphiTilde{}'.format(minJetPt), default_value = 99))
        ret.append(tan(srcName = 'jet{}_chi'.format(minJetPt), outName = 'jet{}_tanChi'.format(minJetPt)))
        ret.append(minimum(srcName = 'jet{}_tanChi'.format(minJetPt), outName = 'minTanChi{}'.format(minJetPt), default_value = 99))

        ret.append(jetDphiAttrs(inJetPrefix = 'jetJECUp', outJetPrefix = 'jetJECUp{}'.format(minJetPt), minJetPt = minJetPt))
        ret.append(minimum(srcName = 'jetJECUp{}_chi'.format(minJetPt), outName = 'minChi{}JECUp'.format(minJetPt), default_value = -1))
        ret.append(jetDphiAttrs(inJetPrefix = 'jetJECDown'.format(minJetPt), outJetPrefix = 'jetJECDown{}'.format(minJetPt), minJetPt = minJetPt))
        ret.append(minimum(srcName = 'jetJECDown{}_chi'.format(minJetPt), outName = 'minChi{}JECDown'.format(minJetPt), default_value = -1))

    ##
    ## from Scribblers.scratch import scratch
    ## ret.append(scratch())

    ##
    ret.append(metNoX())

    ret.append(njetnbjetbin())
    ret.append(htbin())
    ret.append(MhtOverMet())
    ret.append(MhtOverMetNoX())

    if metnohf:
        ret.append(metNoXNoHF())
        ret.append(MhtOverMetNoHF())
        ret.append(MhtOverMetNoXNoHF())

    return ret

##__________________________________________________________________||
