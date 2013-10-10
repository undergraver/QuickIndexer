import sys
import os

thisdir=os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(thisdir))

import Common

def CreateDatabase(fileName):
    if fileName is None:
        fileName = Common.GetDefaultDbFile()

    if os.path.exists(fileName):
        os.unlink(fileName)

    db = Common.DBAccess(fileName)

    # get the path of this directory
    thisdir=os.path.abspath(os.path.dirname(__file__))

    sqlScript = thisdir + os.sep + 'sqliteInit.sql'

    db.ExecuteSQLScriptFile(sqlScript)

if __name__=="__main__":
    database = Common.GetDefaultDbFile()
    CreateDatabase(database)

