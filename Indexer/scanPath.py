class ScanPath:
    def __init__(self,keyval={}):
        self.kv=keyval

    def __getattr__(self,key):
        #print "__getattr__ %s" % (key)
        #print type(self.kv[key])
        return self.kv[key]

    def getitem(self,key):
        #print "getitem %s" % (key)
        return self.kv[key]

def GetScanPaths(db):
    results = db.ExecuteSQLCommand("SELECT * FROM scanpaths")

    scanpaths=[]

    for r in results:
        scanpath = ScanPath(r)
        scanpaths.append(scanpath)

    return scanpaths


