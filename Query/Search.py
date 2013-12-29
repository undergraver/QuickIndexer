import os
import sys

from Common import *

def Search(dbFile, patternType, patterns, maxresults):
    if dbFile is None:
        dbFile = GetDefaultDbFile()
    db = DBAccess(dbFile)

    # TODO: in case of maxresults also
    # take care of the offset - see OFFSET from sql limit documentation
    if maxresults is None:
        maxresults = 0

    if len(patterns) == 0:
        # nothing to search for
        return []

    results = []
    sql = "SELECT filepath from files WHERE "

    patternCount = len(patterns)

    for i in range(patternCount):

        pattern = patterns[i]
        patternCondition = SQLPatternCondition(patternType, pattern, 'filepath')
        sql += patternCondition

        last = (i+1 == patternCount)
        if not last:
            sql += " OR "

    if maxresults > 0:
        sql += " LIMIT %d" % (maxresults)

    #print sql
    results = db.ExecuteSQLCommand(sql)

    return [row['filepath'] for row in results]


def SQLPatternCondition(patternType, pattern, columnName):

    if patternType == 'glob':
        return "%s GLOB '%s'" % (columnName, pattern)
    elif patternType == 'iglob':
        # keep existing _ ; ( _ -> \_ )
        # keep existing % ; ( % -> \% )
        # transform to "like" ( * -> % ) and ( ? -> _ )
        likepattern = pattern.replace('_','\_')
        likepattern = likepattern.replace('%','\%')
        likepattern = likepattern.replace('*','%')
        likepattern = likepattern.replace('?','_')
        return "%s LIKE '%s' ESCAPE '\\'" % (columnName, likepattern)
    elif patternType == 'like':
        return "%s LIKE '%s' ESCAPE '\\'" % (columnName, pattern)
    elif patternType == 'regex':
        raise Exception("Not implemented")
    elif patternType == "iregex":
        raise Exception("Not implemented")
    else:
        raise Exception("Unknown pattern type:"+patternType)

