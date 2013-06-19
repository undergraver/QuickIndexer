#!/bin/sh

DBFILE=sqlitedata.db

sqlite3 $DBFILE < sqliteInit.sql
