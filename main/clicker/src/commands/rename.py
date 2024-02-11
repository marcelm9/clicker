from sys import exit
from ..database.database import Database
from ..log import Log

def synopsis():
    Log.info("SYNOPSIS:")
    Log.info("clicker rename <old_name> <new_name>")
    exit(1)

def rename(args):
    if len(args) != 2:
        synopsis()

    name_old = args[0]
    name_new = args[1]

    if name_old + ".txt" not in Database.get_all_names():
        Log.error(f"No file with name '{name_old}' found in database")
        exit(1)
    
    if name_new + ".txt" in Database.get_all_names():
        Log.error(f"File with name '{name_new}' already exists in database")
        exit(1)

    Database.rename(args[0], args[1])
    Log.info(f"Renamed '{args[0]}' to '{args[1]}'")
