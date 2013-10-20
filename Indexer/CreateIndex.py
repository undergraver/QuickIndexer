#!/usr/bin/env python

import sys
import os

thisdir=os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(thisdir))

import scanJob
from Common import *

def UpdateDatabase(dbFile=None,quiet=False):
    if dbFile is None:
        dbFile = Common.GetDefaultDbFile()
    #print database
    db = Common.DBAccess(dbFile)
    scanpaths = db.GetScanPaths()

    for scanpath in scanpaths:
        scanJob.DoScanJob(db,scanpath)

if __name__=="__main__":
    UpdateDatabase()

