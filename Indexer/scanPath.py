import os
import sqlite3

class ScanPath:
    def __init__(self,id=0,path='',pathtype='',username='',password='',globexclusion='',regexexclusion=''):
        self.id=id
        self.path=path
        self.pathtype=pathtype
        self.username=username
        self.password=password
        self.globexclusion=globexclusion
        self.regexexclusion=regexexclusion

def GetScanPaths(database):
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scanpaths")
    results = cursor.fetchall()

    scanpaths=[]

    for r in results:
        scanpath = ScanPath(r['id'],r['path'],r['pathtype'],r['username'],r['password'],r['globexclusion'],r['regexexclusion'])
        scanpaths.append(scanpath)

    return scanpaths


