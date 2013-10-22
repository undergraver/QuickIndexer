#!/usr/bin/env python

import sys
import os

import scanJob
from Common import *

def UpdateDatabase(dbFile=None,quiet=False):
    if dbFile is None:
        dbFile = GetDefaultDbFile()
    #print database
    db = DBAccess(dbFile)
    scanpaths = db.GetScanPaths()

    for scanpath in scanpaths:
        scanJob.DoScanJob(db,scanpath)

if __name__=="__main__":
    UpdateDatabase()

