import os
import fileScan
import smbScan
import Common

def DoScanJob(db,scanpath):

    db.ExecuteSQLCommand('BEGIN')

    # delete previous scanjobs containing the scanpath id
    db.ExecuteSQLCommand("DELETE FROM scanjobs WHERE scanpathid=?",(scanpath.id,))

    results = db.ExecuteSQLCommand("INSERT INTO scanjobs (startdate,status,scanpathid) VALUES (CURRENT_TIMESTAMP,'Working',?)",(scanpath.id,))

    scanjobid=db.GetLastRowId()
    errText="OK"

    if scanpath.pathtype == 'file':
        fileScan.scan(db,scanjobid,scanpath)
    if scanpath.pathtype == 'smb':
        smbScan.scan(db,scanjobid,scanpath)

    db.ExecuteSQLCommand("UPDATE scanjobs SET enddate=CURRENT_TIMESTAMP,status='Done',result=? WHERE id=?",(errText,scanjobid))

    db.ExecuteSQLCommand('END')


