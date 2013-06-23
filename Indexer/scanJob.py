import os
import fileScan

def DoScanJob(db,scanpath):
    if scanpath.pathtype == 'file':

        db.ExecuteSQL('BEGIN')

        results = db.ExecuteSQL("INSERT INTO scanjobs (startdate,status,scanpathid) VALUES(CURRENT_TIMESTAMP,'Working',?)",(scanpath.id,))

        scanjobid=db.GetLastRowId()

        errText="OK"
        fileScan.scan(db,scanjobid,scanpath.path)
        
        db.ExecuteSQL("UPDATE scanjobs SET enddate=CURRENT_TIMESTAMP,status='Done',result=? WHERE id=?",(errText,scanjobid))

        db.ExecuteSQL('END')



