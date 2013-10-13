from Common import *

def AddScanPath(fileName,path,pathType,user,password,excNameGlob,excNameRegex,excPathGlob,excPathRegex):
    db = GetDbAccessHandle(fileName)
    db.AddScanPath(path,pathType,user,password,excNameGlob,excNameRegex,excPathGlob,excPathRegex)

def GetScanPaths(fileName,pathId):
    db = GetDbAccessHandle(fileName)
    paths = db.GetScanPaths(pathId)

    buf = ""
    for path in paths:
        s = "Scan path " + path["id"]
        buf += s
        
