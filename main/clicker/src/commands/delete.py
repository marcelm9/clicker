from sys import exit
from ..database.database import Database
from ..log import Log

def synopsis():
    Log.info("SYNOPSIS:")
    Log.info("clicker delete <name>")
    exit(1)

def delete(args):
    if len(args) != 1:
        synopsis()

    name = args[0]

    if name + ".txt" not in Database.get_all_names():
        Log.error(f"No file with name '{name}' found in database")

    Database.delete(args[0])
    Log.info(f"Deleted file '{args[0]}'")
