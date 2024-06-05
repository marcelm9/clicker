from sys import exit
from ..log import Log
from ..database.database import Database

def synopsis():
    Log.info("SYNOPSIS")
    Log.info("clicker clear")
    exit(1)

def clear(args):
    if len(args) > 0:
        synopsis()

    if (l := len(Database.get_all_names())) == 0:
        Log.info("No files in database")
        exit(0)

    count = 3
    while count > 0 and (ans := Log.ask("Are you sure you want to clear the database? \[y/n] ")).lower() not in ["y", "n"]:
        count -= 1

    if count == 0:
        Log.error("Aborting")
        exit(1)

    if ans == "n":
        Log.info("Aborting")
        exit(0)

    elif ans == "y":
        Database.clear()
        Log.info(f"Deleted {l} files")
