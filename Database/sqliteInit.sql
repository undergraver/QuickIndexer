PRAGMA foreign_keys = ON;

-- paths table; paths present here are scanned and indexed
-- into the database

CREATE TABLE IF NOT EXISTS scanpaths (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    path TEXT,
    pathtype TEXT,
    username TEXT,
    password TEXT,
    globexclusion_name TEXT,
    regexexclusion_name TEXT,
    globexclusion_path TEXT,
    regexexclusion_path TEXT
);

-- scan jobs table; a scan job is the operation of scanning
-- a path referref by the scanpaths table

CREATE TABLE IF NOT EXISTS scanjobs (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    startdate DATE,
    enddate DATE,
    status TEXT,
    result TEXT,
    scanpathid INTEGER,
    FOREIGN KEY(scanpathid) REFERENCES scanpaths(id),
    CHECK (status IN ("Working","Done") )
);

-- files table; files are stored in the database while scanning

CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    filepath TEXT,
    scanjobid INTEGER,
    FOREIGN KEY(scanjobid) REFERENCES scanjobs(id)
);

-- trigger to delete all the jobs associated with a deleted path

CREATE TRIGGER IF NOT EXISTS deletejobs_referring_deleted_scanpaths
AFTER DELETE ON scanpaths
BEGIN
    DELETE FROM scanjobs WHERE scanpathid = OLD.id;
END;

-- trigger to delete all the files associated with a deleted job

CREATE TRIGGER IF NOT EXISTS delete_files_referring_deleted_jobs
AFTER DELETE ON scanjobs
BEGIN
    DELETE FROM files WHERE scanjobid = OLD.id;
END;

