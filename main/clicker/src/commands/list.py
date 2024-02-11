from sys import exit
from ..database.database import Database
from ..log import Log

def synopsis():
    Log.info("SYNOPSIS:")
    Log.info("clicker list")
    exit(1)

def list_(args):
    if len(args) != 0:
        synopsis()

    names = Database.get_all_names()
    
    if len(names) == 0:
        Log.info("No files found in database")
    
    else:
        Log.info("Files in database")
        for name in names:
            Log.info(f" - {name.removesuffix('.txt')}")
