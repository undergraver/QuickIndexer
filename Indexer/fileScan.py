# scans paths of type 'file' (file systems)

import os
from Common import *

#file:// + path

def scan(db,scanjobid,scanpath):
    path=scanpath.path

    namefilter,pathfilter = CreateFiltersForScanpath(scanpath)

    scan_recursively(db,scanjobid,path,namefilter,pathfilter)

def scan_recursively(db,scanjobid,path,namefilter,pathfilter):
    try:
        files = os.listdir(path)
    except Exception as e:
        print "Failed scanning %s; reason: %s" % (path,str(e))
        return

    for f in files:
        newpath = os.path.join(path,f)
	isDirectory = os.path.isdir(newpath)

        if os.path.islink(newpath):
            continue

        if namefilter.IsMatching(f):
            # name found in name exclusion filter
            continue

        if pathfilter.IsMatching(newpath):
            # path found in path exclusion filter
            continue

        db.StoreFile(scanjobid,newpath)

        if isDirectory:
            # go deeper recursively
            scan_recursively(db,scanjobid,newpath,namefilter,pathfilter)


