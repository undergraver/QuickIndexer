# scans paths of type 'file' (file systems)

import os
import fileFilter

def storeFile(db,scanjobid,path):
    db.ExecuteSQLCommand("INSERT INTO FILES (filepath,scanjobid) VALUES(?,?)",(path,scanjobid))

def scan(db,scanjobid,scanpath):
    path=scanpath.path

    glob_name = scanpath.globexclusion_name.split('\r')
    regex_name = scanpath.regexexclusion_name.split('\r')
    namefilter=fileFilter.createFilter(glob_name,regex_name)

    glob_path = scanpath.globexclusion_path.split('\r')
    regex_path = scanpath.regexexclusion_path.split('\r')

    pathfilter=fileFilter.createFilter(glob_path,regex_path)

    scan_recursively(db,scanjobid,path,namefilter,pathfilter)

def scan_recursively(db,scanjobid,path,namefilter,pathfilter):
    try:
        files = os.listdir(path)
    except Exception as e:
        print "Failed scanning %s; reason: %s" % (path,str(e))
        return

    for f in files:
        newpath = os.path.join(path,f)

        storeFile(db,scanjobid,newpath)

        if os.path.islink(newpath):
            continue

        if namefilter != None and namefilter.IsMatching(f):
            # name found in name exclusion filter
            continue

        if pathfilter != None and pathfilter.IsMatching(newpath):
            # path found in path exclusion filter
            continue

        if os.path.isdir(newpath):
            # go deeper recursively
            scan_recursively(db,scanjobid,newpath,namefilter,pathfilter)


