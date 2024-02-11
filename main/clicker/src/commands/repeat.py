from .play import play
from ..log import Log
from ..database.database import Database
from sys import exit
import time

def synopsis():
    Log.info("SYNOPSIS:")
    Log.info("clicker repeat <name> <count> <wait>")
    exit(1)

def repeat(args):
    if len(args) != 3:
        synopsis()

    name = args[0]
    if name + ".txt" not in Database.get_all_names():
        Log.error(f"Could not find file '{name}' in database")
        exit(1)
    try:
        count = int(args[1])
    except:
        Log.error(f"Could not interpret '{args[1]}' as integer")
        exit(1)
    try:
        wait = float(args[2])
    except:
        Log.error(f"Could not interpret '{args[2]}' as float")
        exit(1)

    if count < 1:
        Log.error("<count> needs to be higher than 0")
        exit(1)
    if count < 0:
        Log.error("<wait> needs to be higher or equal to 0")

    Log.info(f"Starting repeat for file '{name}' {count} time(s) with wait of {wait} seconds")
    play([name])
    for _ in range(count - 1):
        if wait > 0:
            Log.info(f"Waiting for {wait} seconds")
            time.sleep(wait)
        play([name])

    Log.info("Repeat finished")
