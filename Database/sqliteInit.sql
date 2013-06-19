PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS paths (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT, 
    scanpath TEXT,
    pathtype TEXT,
    globexclusion TEXT,
    regexexclusion TEXT
);

CREATE TABLE IF NOT EXISTS scanjobs (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    startdate DATE,
    enddate DATE,
    pathid INTEGER,
    FOREIGN KEY(pathid) REFERENCES paths(id)
);

CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    filepath TEXT,
    scanjobid INTEGER,
    FOREIGN KEY(scanjobid) REFERENCES scanjobs(id)
);

