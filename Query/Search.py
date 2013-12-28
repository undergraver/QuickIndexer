import os
import sys

from Common import *

def Search(dbFile, patternType, patterns, maxresults):
    if dbFile is None:
        dbFile = GetDefaultDbFile()
    db = DBAccess(dbFile)

    if maxresults is None:
        maxresults = 0

    if maxresults is None:
        maxresults = 0

    results = []

    for pattern in patterns:
        tempresults = SearchPattern(db, patternType, pattern, maxresults)
        results += tempresults;
        if maxresults > 0:
            maxresults -= len(results)
            if maxresults <= 0:
                # done obtaining the limited results
                break

    return results


def SearchPattern(db, patternType, pattern, maxresults):

    sqlAppendLimit = ""
    if maxresults > 0:
        sqlAppendLimit = " LIMIT %d" % (maxresults)


    sql = ""
    if patternType == 'glob':
        sql = "SELECT filepath from files WHERE filepath GLOB '%s'" % pattern
    elif patternType == 'iglob':
        # TODO: transform to "like" * -> %, ? -> _
        raise Exception("Not implemented")
    elif patternType == 'like':
        sql = "SELECT filepath from files WHERE filepath LIKE '%s'" % pattern
    elif patternType == 'regex':
        raise Exception("Not implemented")
    elif patternType == "iregex":
        raise Exception("Not implemented")
    else:
        raise Exception("Unknown pattern type:"+patternType)

    sql += sqlAppendLimit

    results = db.ExecuteSQLCommand(sql)

    return [row['filepath'] for row in results]
