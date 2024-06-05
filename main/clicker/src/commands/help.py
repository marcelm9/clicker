from sys import exit
from ..log import Log

def help(args):
    if len(args) > 0:
        Log.error("too many arguments")
        exit(1)
    
    Log.info("Commands:")
    Log.info(" - help")
    Log.info(" - list")
    Log.info(" - play")
    Log.info(" - record")
    Log.info(" - rename")
    Log.info(" - delete")
    Log.info(" - show")
    Log.info(" - clear")
    Log.info(" - repeat")
