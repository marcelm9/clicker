from sys import exit
from ..database.database import Database
from ..log import Log

def synopsis():
    Log.info("SYNOPSIS:")
    Log.info("clicker show <name>")
    exit(1)

def show(args):
    if len(args) != 1:
        synopsis()

    name = args[0]

    if name + ".txt" not in Database.get_all_names():
        Log.error(f"No file with name '{name}' found in database")
        exit(1)

    Log.info(f"File '{name}':")
    for line in Database.show(name):
        Log.info(line.removesuffix("\n"))
