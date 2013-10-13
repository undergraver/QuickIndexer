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
        self.ExecuteSQLScript(sqlscript)

    def ExecuteSQLScript(self,sqlscript):
        self.cursor.executescript(sqlscript)

    def GetLastRowId(self):
        return self.cursor.lastrowid

    def StoreFile(self,scanjobid,path):
        self.ExecuteSQLCommand("INSERT INTO FILES (filepath,scanjobid) VALUES(?,?)",(path,scanjobid))

    def AddScanPath(self,path,pathType,user,password,excNameGlob,excNameRegex,excPathGlob,excPathRegex):
        if pathType is None:
            pathType = GetDefaultPathType()

        if user is None:
            user = ''

        if password is None:
            password = ''

        if excNameGlob is None:
            excNameGlob = []

        if excNameRegex is None:
            excNameRegex = []

        if excPathGlob is None:
            excPathGlob = []

        if excPathRegex is None:
            excPathRegex = []

        excNameGlobDb = '\r'.join(excNameGlob)
        excNameRegexDb = '\r'.join(excNameRegex)

        excPathGlobDb = '\r'.join(excPathGlob)
        excPathRegexDb = '\r'.join(excPathRegex)

        self.ExecuteSQLCommand("INSERT INTO scanpaths (path,pathtype,username,password,globexclusion_name,regexexclusion_name,globexclusion_path,regexexclusion_path) VALUES(?,?,?,?,?,?,?,?)",(path,pathType,user,password,excNameGlobDb,excNameRegexDb,excPathGlobDb,excPathRegexDb))

    def GetScanPaths(self,pathId=None):
        if pathId is None:
            return self.GetAllScanPaths()

        return self.GetPathWithId(pathId)

    def GetAllScanPaths(self):
        return self.ExecuteSQLCommand("SELECT * FROM scanpaths")
    
    def GetPathWithId(self,pathId):
        return self.ExecuteSQLCommand("SELECT * FROM scanpaths WHERE id=?",(pathId,))

