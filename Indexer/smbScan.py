# scan paths of type smb

# To use this you must install:
# pysmb
# pyasn1

# smb:// + path
# where path=computername/share/path_in_share

from smb.SMBConnection import SMBConnection
from smb.base import SharedDevice
from smb.base import SharedFile
import socket

class SMBUtility:
    def __init__(self,computer,username,password):
        self.computer = computer
        self.username = username
        self.password = password
        self.conn = None

    def Connect(self):
        client_machine_name = socket.gethostname()
        # watch out:
        # self.computer is unicode (must be converted to str)!
        conn = SMBConnection(self.username,self.password,client_machine_name,str(self.computer))

        computerIp = socket.gethostbyname(self.computer)
        #print computerIp

        conn.connect(computerIp,139)

        self.conn = conn

    def GetFileShareList(self):
        returnList = []
        try:
            if self.conn is None:
                self.Connect()

            shares = self.conn.listShares()

            returnList = [share.name for share in shares if share.type == ShareDevice.DISK_TREE ]
        except:
            pass

        return returnList

    def ListPath(self,share,sharePath):
        lst = []
        try:
            print share
            print sharePath
            if self.conn is None:
                self.Connect()
            lst = self.conn.listPath(share,sharePath)
        except Exception as e:
            print str(e)

        return lst

def scan(db,scanjobid,scanpath):
    path=scanpath.path

    computerName = ''
    shareName = ''
    sharePath = ''
    
    splitPath = path.split('/',2)
    if len(splitPath) > 0:
        computerName = splitPath[0]

    if len(splitPath) > 1:
        shareName = splitPath[1]

    if len(splitPath) > 2:
        sharePath = splitPath[2]

    if computerName == '':
        # no computer name specified
        return

    utility = SMBUtility(computerName,scanpath.username,scanpath.password)

    shareList = []

    if shareName != '':
        shareList = [shareName]
    else:
        shareList = utility.GetFileShareList()

    if len(shareList) == 0:
        # no file shares
        return

    sharePaths = []

    if sharePath == '':
        sharePath = '/'

    # we always have a share path
    # in case we have more than a share the sharePath should be '/'
    for share in shareList:
        scanShare(utility,share,sharePath)

def scanShare(utility,share,sharePath):
    sharedFiles = utility.ListPath(share,sharePath)
    for f in sharedFiles:
        print f.filename + "; " + str(f.file_attributes) + "; " + str(f.isDirectory)


