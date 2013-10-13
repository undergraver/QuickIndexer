import Defaults
from DBAccess import *
import FileFilter

def GetDbAccessHandle(fileName):
    if fileName is None:
        fileName = Defaults.GetDefaultDbFile()

    return DBAccess(fileName)

def CreateFiltersForScanpath(scanpath):
    glob_name = scanpath.globexclusion_name.split('\r')
    regex_name = scanpath.regexexclusion_name.split('\r')
    namefilter=FileFilter.CreateFilter(glob_name,regex_name)

    glob_path = scanpath.globexclusion_path.split('\r')
    regex_path = scanpath.regexexclusion_path.split('\r')
    pathfilter=FileFilter.CreateFilter(glob_path,regex_path)

    return (namefilter,pathfilter)

