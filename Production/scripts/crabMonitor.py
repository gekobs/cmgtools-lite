#!/usr/bin/env python
import os
import time
import glob
from collections import OrderedDict as odict

import pandas as pd
pd.options.display.max_rows = 100
pd.options.display.width = 160

##____________________________________________________________________________||
def parse_args():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("crab_tasks", nargs="+",
                        help="Input paths (with wildcards) for the crab tasks "
                        "to check their status")
    parser.add_argument("-r", "--resubmit", default=False, action="store_true",
                        help="Auto resubmit failed jobs")

    args = parser.parse_args()
    return args

##____________________________________________________________________________||
def bash_command(command):
    import subprocess as sp
    proc = sp.Popen(command.split(), stdout=sp.PIPE, stderr=sp.PIPE)
    return proc.communicate()

##____________________________________________________________________________||
def checkStatusTask(task, types):
    log, err = bash_command('crab status -d {}'.format(task))

    taskName = ""
    dataset = ""
    jobInfos = {key: 0 for key in types}
    jobInfos["increase_wall_time"] = False

    for line in log.splitlines():
        if "failed with exit code 50664" in line:   
            jobInfos["increase_wall_time"] = True

        if " SUBMITFAILED" in line:
            print "ERROR: SUBMITFAILED for {}".format(task)
            return None

        if "Cannot find .requestcache" in line:
            print "Cannot find .requestcache in {}".format(task)
            return None

        if "Task name" in line:
            taskName = line.split(":")[2]
            user     = taskName.split("_")[0]
            dataset  = "_".join(taskName.split("_")[2:-1])

        if "timed out" in line: #error of communication, bypass
            return None

        if len(line.split("("))>1 and "/" in line and "Warning" not in line:
            tmp = line.split("(")[1][:-1]
            print "\n\n tmp : ",tmp
            nJobs = int(tmp.split("/")[0])
            jobInfos["total"] = int(tmp.split("/")[1])

            for report_key, crab_keys in types.iteritems():
                if any(True for crab_key in crab_keys if crab_key in line):
                    jobInfos[report_key] = nJobs

    jobInfos.update({"dataset": dataset})
    return jobInfos

##____________________________________________________________________________||
def crabResubmit(task, increase_wall_time=False):
    command = "crab resubmit -d {}".format(task)
    if increase_wall_time:
        command += " --maxjobruntime 4320"
    return bash_command(command)

##____________________________________________________________________________||
def prepareReport(tasks, resubmit):
    types = odict([
        ("run",      ["running"]),
        ("done",     ["finished", "transferred"]),
        ("transfer", ["transferring"]),
        ("wait",     ["unsubmitted", "idle"]),
        ("fail",     ["failed"]),
        ("total",    []),
    ])

    job_data = []
    for task in tasks:
        jobInfos = checkStatusTask(task, types)
        if jobInfos!=None:
            dataset = jobInfos["dataset"]

            if jobInfos["total"]==0:
                print "ERROR: unable to retrieve the jobs for the task " \
                      "{}".format(dataset)
                continue

            if jobInfos["fail"]>0 and resubmit:
                print "WARNING: dataset {} shows failed jobs ({}/{}) -> " \
                      "automatic resubmission".format(dataset,
                                                      jobInfos["fail"],
                                                      jobInfos["total"])
                crabResubmit(task, jobInfos["increase_wall_time"])

            job_data.append(jobInfos)

    job_dataframe = pd.DataFrame(job_data, columns=["dataset"]+types.keys())
    curTime = time.strftime("%H:%M:%S")
    curDate = time.strftime("%d/%m/%Y")
    sum_dataframe = pd.DataFrame(job_dataframe.sum()).T
    sum_dataframe["dataset"] = "Total"
    print "\nProduction report: {} ({})\n".format(curDate, curTime)
    print pd.concat([job_dataframe, sum_dataframe])

##____________________________________________________________________________||
def crabAutoTool(options):
    tasks = []
    for task in options.crab_tasks:
        if "*" in task:
            tasks.extend(sorted(glob.glob(task)))
        else:
            if os.path.exists(task):
                tasks.append(task)
    prepareReport(tasks, options.resubmit)

##____________________________________________________________________________||
if __name__ == "__main__":
    opts = parse_args()
    crabAutoTool(opts)