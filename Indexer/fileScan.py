# scans paths of type 'file' (file systems)

import os

def storeFile(db,scanjobid,path):
    db.ExecuteSQL("INSERT INTO FILES (filepath,scanjobid) VALUES(?,?)",(path,scanjobid))

def scan(db,scanjobid,path):
    files = os.listdir(path)
    for f in files:
        newpath = os.path.join(path,f)

        storeFile(db,scanjobid,newpath)

        if os.path.islink(newpath):
            continue

        # TODO: Use filters

        if os.path.isdir(newpath):
            # go deeper recursively
            scan(db,scanjobid,newpath)


