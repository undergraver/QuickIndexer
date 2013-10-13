from Common import *

def AddScanPath(fileName,path,pathType,user,password,excNameGlob,excNameRegex,excPathGlob,excPathRegex):
    db = GetDbAccessHandle(fileName)
    db.AddScanPath(path,pathType,user,password,excNameGlob,excNameRegex,excPathGlob,excPathRegex)

def ShowScanPaths(fileName,pathId):
    db = GetDbAccessHandle(fileName)
    paths = db.GetScanPaths(pathId)

    buf = ""
    for path in paths:
        s = "Scan path " + str(path["id"]) + " configuration\n"
        buf += s
        s = "Path:"+str(path['path']) + "\n"
        buf += s
        s = "Type:"+str(path['pathtype']) + "\n"
        buf += s
        s = "User:" + str(path['username']) + "\n"
        buf += s
        s = "Password:" + str(path['password']) + "\n"
        buf += s

        nameglobs = path['globexclusion_name'].split('\r')
        s = "Name exclude globs:" + ','.join(nameglobs) + "\n"
        buf += s

        nameregex = path['regexexclusion_name'].split('\r')
        s = "Name exclude regex:" + ','.join(nameregex) + "\n"
        buf += s

        pathglobs = path['globexclusion_path'].split('\r')
        s = "Path exclude globs:" + ','.join(pathglobs) + "\n"
        buf += s

        pathregex = path['regexexclusion_path'].split('\r')
        s = "Path exclude regex:" + ','.join(pathregex) + "\n"
        buf += s

        buf += "-----------\n"

    print buf

def DeleteScanPaths(fileName,pathId):
    db = GetDbAccessHandle(fileName)
    db.RemoveScanPaths(pathId)

