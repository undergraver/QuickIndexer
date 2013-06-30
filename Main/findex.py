#!/usr/bin/env python

import argparse
import sys

def DoMain():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    # (re)create the database 
    createparser = subparsers.add_parser('create')
    createparser.add_argument("-f","--file",required=False,help="the database file name to be created")
    
    # update the database
    updateparser = subparsers.add_parser('update')
    updateparser.add_argument("-q","--quiet",action='store_true',required=False,help="be quiet; do not display messages")
    
    configparser = subparsers.add_parser("config")
    
    subconfig = configparser.add_subparsers()
    addparser = subconfig.add_parser("add")
    addparser.add_argument("--path",required=True,help="the path to add")
    addparser.add_argument("--type",required=False,default='file',choices=['file','smb','ftp'],help="the type of path")
    addparser.add_argument("--user",required=False,help="the user needed to log on")
    addparser.add_argument("--password",required=False,help="the password needed to log on")
    addparser.add_argument("--exclude-name-glob",required=False,action='append',help="exclusion name pattern as glob")
    addparser.add_argument("--exclude-name-regex",required=False,action='append',help="exclusion name pattern as regex")
    addparser.add_argument("--exclude-path-glob",required=False,action='append',help="exclusion path pattern as glob")
    addparser.add_argument("--exclude-path-regex",required=False,action='append',help="exclusion path pattern as regex")
    
    viewparser = subconfig.add_parser("view")
    editparser = subconfig.add_parser("edit")
    deleteparser = subconfig.add_parser("delete")
    
    searchparser = subparsers.add_parser("search")
    searchparser.add_argument("--glob",required=False,action='append',help="the glob pattern to match",metavar="glob")
    searchparser.add_argument("--regex",required=False,action='append',help="the regex pattern to match")
    searchparser.set_defaults(func=DoSearch)

    print parser.parse_args()

def DoDatabaseCreate(args):
    print "DoDatabaseCreate:"
    print args

def DoDatabaseUpdate(args):
    print "DoDatabaseUpdate:"
    print args
    
def DoConfigAdd(args):
    print "DoConfigAdd"
    print args
    
def DoConfigView(args):
    print "DoConfigView"
    print args
    
def DoConfigEdit(args):
    print "DoConfigEdit"
    print args

def DoConfigDelete(args):
    print "DoConfigDelete"
    print args

def DoSearch(args):
    print "DoSearch"
    print args

if __name__=="__main__":
    DoMain()
