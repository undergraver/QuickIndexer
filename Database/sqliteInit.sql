PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS paths (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT, 
    scanpath TEXT,
    username TEXT,
    password TEXT,
    pathtype TEXT,
    globexclusion TEXT,
    regexexclusion TEXT
);

CREATE TABLE IF NOT EXISTS scanjobs (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    startdate DATE,
    enddate DATE,
    status TEXT,
    result TEXT,
    pathid INTEGER,
    FOREIGN KEY(pathid) REFERENCES paths(id),
    CHECK (status IN ("Working","Done") )
);

CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    filepath TEXT,
    scanjobid INTEGER,
    FOREIGN KEY(scanjobid) REFERENCES scanjobs(id)
);

CREATE TRIGGER IF NOT EXISTS deletejobs_referring_deleted_paths
AFTER DELETE ON paths
BEGIN
    DELETE FROM scanjobs WHERE pathid = OLD.id;
END;

