import sqlite3

class DBAccess:
    def __init__(self,dbfile):
        self.dbfile = dbfile
        self.InitSQLite()

    def __del__(self):
        self.connection.commit()
        self.connection.close()
        self.connection=None
        self.cursor=None
        self.dbfile=None

    def InitSQLite(self):
        self.connection = sqlite3.connect(self.dbfile)
        self.connection.isolation_level = None
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        self.ExecuteSQLCommand('PRAGMA foreign_keys=ON')
        self.ExecuteSQLCommand('PRAGMA synchronous=NORMAL')
        self.ExecuteSQLCommand('PRAGMA journal_mode=WAL')
        self.ExecuteSQLCommand('PRAGMA ignore_check_constraints=off')

    def ExecuteSQLCommand(self,query,parameters=[]):
        self.cursor.execute(query,parameters)
        # return the execution results
        return self.cursor.fetchall()

    def ExecuteSQLScriptFile(self,filename):
        sqlscript=open(filename,'r').read()
        ExecuteSQLScript(sqlscript)

    def ExecuteSQLScript(self,sqlscript):
        self.cursor.executescript(sqlscript)

    def GetLastRowId(self):
        return self.cursor.lastrowid


