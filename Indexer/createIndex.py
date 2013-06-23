#!/usr/bin/env python

import sys
import os

thisdir=os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(thisdir))

import scanPath
import scanJob
import Common

if __name__=="__main__":
    database = os.getenv('HOME') + "/.fileIndex.db"
    db = Common.DBAccess(database)
    scanpaths = scanPath.GetScanPaths(db)

    for scanpath in scanpaths:
        scanJob.DoScanJob(db,scanpath)

