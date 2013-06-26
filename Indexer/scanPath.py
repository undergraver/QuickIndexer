
class ScanPath:
    def __init__(self,keyval={}):
        self.kv=keyval

    def __getattr__(self,key):
        #print "__getattr__ %s" % (key)
        return self.kv[key]

    def getitem(self,key):
        #print "getitem %s" % (key)
        return self.kv[key]

def GetScanPaths(db):
    results = db.ExecuteSQL("SELECT * FROM scanpaths")

    scanpaths=[]

    for r in results:
        scanpath = ScanPath(r)
        scanpaths.append(scanpath)

    return scanpaths


