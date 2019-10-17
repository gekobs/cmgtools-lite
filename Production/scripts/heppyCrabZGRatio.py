#!/usr/bin/env python
import imp
import os
import json
import argparse

##____________________________________________________________________________||
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--cutFlow', default="AtLogic_Data",
                        help="Standard cfg file to be run. For multiple "
                        "choices separate by spaces")
    parser.add_argument('-s', '--storage-site', dest="storageSite",
                        help="Site where the output should be staged out "
                        "(e.g. T2_UK_London_IC or T2_UK_SGrid_Bristol)")
    parser.add_argument('--aaa', dest="AAAconfig", default="full",
                        help="AAA configuration: full (free AAA access via "
                        "redirectors), local (for reading from local site, "
                        "will turn AAA and ignoreLocality off), eos (force "
                        "reading from EOS via AAA)")
    parser.add_argument('-d', '--outDir', dest="outputDir", default="heppyFlatTrees",
                        help="Name of the directory where the files will be "
                        "staged out: /store/user/$USER/$outputDir/80X/$label/"
                        "dataset/$date_$time/0000/foo.bar")
    parser.add_argument('-l', '--label', default=None,
                        help="Heppy crab production label")
    parser.add_argument('--dry-run', action="store_true", default=False,
                        help="Do not run any commands")
    parser.add_argument('--ship-file', dest='filesToShip', default=[],
                        nargs='*',
                        help="Additional files to ship to WN (will be placed "
                        "in the same directory as the cfg when running)")

    args = parser.parse_args()
    return args

##____________________________________________________________________________||
if __name__ == "__main__":
    options = parse_args()
    cmssw = os.environ["CMSSW_BASE"]

    # datasets to run as defined from cfg file
    # number of jobs to run per dataset decided based on splitFactor and
    # fineSplitFactor from cfg file
    from PhysicsTools.HeppyCore.framework.heppy_loop import _heppyGlobalOptions
    _heppyGlobalOptions["isCrab"] = True
    optjsonfile = open('options.json','w')
    optjsonfile.write(json.dumps(_heppyGlobalOptions))
    optjsonfile.close()

    os.system("tar czf cmssw.tar.gz --dereference --directory $CMSSW_BASE "
              "python")
    os.system("tar czf cmgdataset.tar.gz --directory $HOME .cmgdataset")
    os.system("cp $CMSSW_BASE/src/CMGTools/Production/tarballs/cafpython.tar.gz .")

    import datetime
    now = datetime.datetime.now()
    os.environ["DATETIME"] = now.strftime("%y%m%d_%H%M%S")
    os.environ["USEAAA"] = options.AAAconfig
    os.environ["STAGEOUTREMDIR"] = options.outputDir
    os.environ["OUTSITE"] = options.storageSite
    os.environ["LABEL"] = options.cutFlow
    if options.label: os.environ["LABEL"] += "_"+options.label
    os.environ["CMG_VERSION"] = "94X"
    #os.environ["FILESTOUNPACK"] = "treeProducerSusyAlphaT/tree.root"
    if len(options.filesToShip)>0:
        os.environ["FILESTOSHIP"] = ','.join(options.filesToShip)

    cfg_path = os.path.join(cmssw, "src/CMGTools/ZGammaRatio/cfg/run_{}_cfg.py".format(options.cutFlow))
    with open(cfg_path, 'r') as handle:
        cfo = imp.load_source(options.cutFlow, cfg_path, handle)
        conf = cfo.config
    os.environ["CFG_FILE"] = cfg_path

    from PhysicsTools.HeppyCore.framework.heppy_loop import split
    for comp in conf.components:
        if getattr(comp,"useAAA",False):
            raise RuntimeError, 'Components should have useAAA disabled in '\
                                'the cfg when running on crab - tune the '\
                                'behaviour of AAA in the crab submission '\
                                'instead!'
        os.environ["DATASET"] = str(comp.name)
        os.environ["NJOBS"] = str(len(split([comp])))

        submission_command = "crab submit -c {}/src/CMGTools/Production/crab/heppy_crab_config_env.py".format(cmssw)
        if options.dry_run: submission_command += " --dryrun"
        os.system(submission_command)

    os.system("rm options.json")
    os.system("rm cmssw.tar.gz")
    os.system("rm cmgdataset.tar.gz")
    os.system("rm cafpython.tar.gz")
