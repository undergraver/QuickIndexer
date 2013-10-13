import os

def GetDefaultDbFile():
    """
    Returns the default path where the database is located
    """
    database = os.getenv('HOME') + "/.fileIndex.db"
    return database


def GetDefaultPathType():
    """
    The default path type is "file"
    Example: file:///home/myuser/Desktop/
    """
    return "file"
