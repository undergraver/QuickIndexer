#!/usr/bin/env python

import os
import scanPath

if __name__=="__main__":
    database = os.getenv('HOME') + "/.fileIndex.db"
    print database
    scanpaths = scanPath.GetScanPaths(database)

    for scanpath in scanpaths:
        scanJob.DoScanJob(scanpath)
    
