import os
cmssw = os.environ["CMSSW_BASE"]

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = os.path.join(cmssw, 'src/CMGTools/Production/crab/heppy_crab_fake_pset.py')
config.JobType.scriptExe = os.path.join(cmssw, 'src/CMGTools/Production/crab/heppy_crab_script.sh')
config.JobType.disableAutomaticOutputCollection = True
# config.JobType.sendPythonFolder = True  #doesn't work, not supported yet? do it by hand

config.JobType.inputFiles = [os.path.join(cmssw, 'src/CMGTools/Production/crab/{}'.format(file_))
                             for file_ in ['FrameworkJobReport.xml', 'heppy_crab_script.py']] + \
                             ['cmgdataset.tar.gz', 'cmssw.tar.gz', 'cafpython.tar.gz', 'options.json']
config.JobType.outputFiles = []

config.Data.inputDBS = 'global'
config.Data.splitting ='EventBased' #'Automatic'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
