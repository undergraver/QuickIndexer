

# To use this you must install:
# pysmb
# pyasn1


from smb.SMBConnection import SMBConnection
from smb.base import SharedDevice
from smb.base import SharedFile

def ListShare(conn,shareName):

    try:
        sharedFiles = conn.listPath(shareName,"/")
        #sharedFiles = conn.listPath(shareName,"/folder")
    except:
        return

    print "Listing share:" + shareName

    for f in sharedFiles:
        print f.filename

conn = SMBConnection("guest","","localhost","localhost")
conn.connect("127.0.0.1",139)

shares = conn.listShares()

for share in shares:
    print "share:" + share.name + ";type=" + str(share.type) + ";comments=" + share.comments
    if share.type == SharedDevice.DISK_TREE:
        ListShare(conn,share.name)

