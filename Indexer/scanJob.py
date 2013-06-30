import os
import fileScan

def DoScanJob(db,scanpath):
    if scanpath.pathtype == 'file':

        db.ExecuteSQLCommand('BEGIN')

        results = db.ExecuteSQLCommand("INSERT INTO scanjobs (startdate,status,scanpathid) VALUES(CURRENT_TIMESTAMP,'Working',?)",(scanpath.id,))

        scanjobid=db.GetLastRowId()

        errText="OK"
        fileScan.scan(db,scanjobid,scanpath)
        
        db.ExecuteSQLCommand("UPDATE scanjobs SET enddate=CURRENT_TIMESTAMP,status='Done',result=? WHERE id=?",(errText,scanjobid))

        db.ExecuteSQLCommand('END')



