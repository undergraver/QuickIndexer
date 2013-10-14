from Common import *

def AddScanPath(fileName,path,pathType,user,password,excNameGlob,excNameRegex,excPathGlob,excPathRegex):
    db = GetDbAccessHandle(fileName)
    db.AddScanPath(path,pathType,user,password,excNameGlob,excNameRegex,excPathGlob,excPathRegex)

def ShowScanPaths(fileName,pathId):
    db = GetDbAccessHandle(fileName)
    paths = db.GetScanPaths(pathId)

    for path in paths:
        path.Display()
        print "-----------\n"

def DeleteScanPaths(fileName,pathId):
    db = GetDbAccessHandle(fileName)
    db.RemoveScanPaths(pathId)

def EditScanPath(fileName,index,path,pathType,user,password,
                delete_name_glob,exclude_name_glob,
                delete_name_regex,exclude_name_regex,
                delete_path_glob,exclude_path_glob,
                delete_path_regex,exclude_path_regex):

    db = GetDbAccessHandle(fileName)
    
    scanpath = db.GetScanPaths(index)[0]

    needUpdate=0

    if path is not None:
        needUpdate+=1
        scanpath.path = path

    if pathType is not None:
        needUpdate+=1
        scanpath.pathtype = pathType

    if user is not None:
        needUpdate+=1
        scanpath.username = user

    if password is not None:
        needUpdate+=1
        scanpath.password = password

    # name
    if delete_name_glob:
        needUpdate+=1
        scanpath.globexclusion_name = ''

    if exclude_name_glob is not None:
        needUpdate+=1
        toappend = '\r'.join(exclude_name_glob)
        if len(scanpath.globexclusion_name) > 0:
            scanpath.globexclusion_name += '\r' + toappend
        else:
            scanpath.globexclusion_name = toappend

    if delete_name_regex:
        needUpdate+=1
        scanpath.regexexclusion_name = ''

    if exclude_name_regex is not None:
        needUpdate+=1
        toappend = '\r'.join(exclude_name_regex)
        if len(scanpath.regexexclusion_name) > 0:
            scanpath.regexexclusion_name += '\r' + toappend
        else:
            scanpath.regexexclusion_name = toappend

    # path
    if delete_path_glob:
        needUpdate+=1
        scanpath.globexclusion_path = ''

    if exclude_path_glob is not None:
        needUpdate+=1
        toappend = '\r'.join(exclude_path_glob)
        if len(path.globexclusion_path) > 0:
            scanpath.globexclusion_path += '\r' + toappend
        else:
            scanpath.globexclusion_path = toappend

    if delete_path_regex:
        needUpdate+=1
        scanpath.regexexclusion_path = ''

    if exclude_path_regex is not None:
        needUpdate+=1
        toappend = '\r'.join(exclude_path_regex)
        if len(scanpath.regexexclusion_path) > 0:
            scanpath.regexexclusion_path += '\r' + toappend
        else:
            scanpath.regexexclusion_path = toappend

    scanpath.Display()

    if needUpdate > 0:
        # only if update needed we update the scanpath information
        db.UpdateScanPath(scanpath)

