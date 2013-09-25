import os
import fileScan
import smbScan

def DoScanJob(db,scanpath):

    db.ExecuteSQLCommand('BEGIN')

    results = db.ExecuteSQLCommand("INSERT INTO scanjobs (startdate,status,scanpathid) VALUES (CURRENT_TIMESTAMP,'Working',?)",(scanpath.id,))

    scanjobid=db.GetLastRowId()
    errText="OK"

    if scanpath.pathtype == 'file':
        fileScan.scan(db,scanjobid,scanpath)
    if scanpath.pathtype == 'smb':
        smbScan.scan(db,scanjobid,scanpath)

    db.ExecuteSQLCommand("UPDATE scanjobs SET enddate=CURRENT_TIMESTAMP,status='Done',result=? WHERE id=?",(errText,scanjobid))

    db.ExecuteSQLCommand('END')

        



