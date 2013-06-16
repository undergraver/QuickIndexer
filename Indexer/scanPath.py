import os

def storeFile(newpath):
    print newpath

def scanPath(path,config=None):
    files = os.listdir()
    for f in files:
        newpath = path + os.sep + f
        if os.path.isdir(newpath):
            # go deeper recursively
            scanPath(newpath,config)
        else:
            storeFile(newpath)


