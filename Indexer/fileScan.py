# scans paths of type 'file' (file systems)

import os

def storeFile(db,scanjobid,path):
    db.ExecuteSQL("INSERT INTO FILES (filepath,scanjobid) VALUES(?,?)",(path,scanjobid))

def scan(db,scanjobid,path):
    files = os.listdir(path)
    for f in files:
        newpath = os.path.join(path,f)

        storeFile(db,scanjobid,newpath)

        # TODO: Use filters and check check for symbolic links

        if os.path.isdir(newpath):
            # go deeper recursively
            scan(db,scanjobid,newpath)


