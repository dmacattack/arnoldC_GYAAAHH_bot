import sys
import time
import datetime

# how to use
# from logging import DBG_MSG, DBG_WRN, DBG_ERR
# DBG_MSG(" this is a debug print ")

# logging flags to control whether or not they are logged
ERR_FLG = True
WRN_FLG = True
MSG_FLG = True
LOGFILE_FLG = False
LOG_FILE = "log.txt"

class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

# write the
def logToFile(text):
   if LOGFILE_FLG:
      f = open(LOG_FILE, "a")
      f.write(text + "\n")
      f.close()

# get te timestamp
def getTimeStamp():
   secsFromBoot = time.time()
   timeStamp = datetime.datetime.fromtimestamp(secsFromBoot).strftime('%Y-%m-%d %H:%M:%S')
   return timeStamp

# debug message function
def DBG_MSG(*args):
   if MSG_FLG:
      print "[M] ", getTimeStamp(), " : " + str(args)
      logToFile("[M] " + getTimeStamp() + " : " + str(args) )

# debug message function
def DBG_WRN(*args):
   if WRN_FLG:
      sys.stdout.write(bcolors.WARNING)
      print "[W] ", getTimeStamp(), " : ", args
      logToFile("[W] " + getTimeStamp() + " : " + str(args) )
      sys.stdout.write(bcolors.ENDC)


# debug message function
def DBG_ERR(*args):
   if ERR_FLG:
      sys.stdout.write(bcolors.FAIL)
      print "[E] ", getTimeStamp(), " : ", args
      logToFile("[E] " + getTimeStamp() + " : " + str(args) )
      sys.stdout.write(bcolors.ENDC)