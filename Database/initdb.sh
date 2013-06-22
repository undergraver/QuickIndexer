#!/bin/sh

DBFILE=$HOME/.fileIndex.db
rm -f $DBFILE

sqlite3 $DBFILE < sqliteInit.sql

