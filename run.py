import praw
from ArnoldLogging import DBG_MSG, DBG_WRN, DBG_ERR
# https://github.com/praw-dev/praw/

# import in the blacklist
BLACKLIST_FILE = open("blackList.txt", "r")
blackList = []
blackList = BLACKLIST_FILE.read().splitlines()
BLACKLIST_FILE.close()

# check if the string contains anything from the blacklist
def containsBlackList(text):
   isBlackList = False

   for i in range(len(blackList)):
      if blackList[i] in text:
         DBG_MSG("string contains blackList item" + blackList[i] )
         isBlackList = True
         break
      else:
         DBG_MSG("keep looking num" + i)
   return isBlackList

# check for code in the post
def checkforcode(text):
   if "<code>" in text:
      return True
   else:
      return False

# print the post
def printPost(post):
   print("--------------------------------------------------------------------------")
   print(" link: %s" %post.link_permalink)
   print(" author: %s" %post.author)
   print(" text: %s" %post.body )
   print(" ################### code ###################" )
   print( post.body_html )
   print("--------------------------------------------------------------------------")

# get the code substring indexes and return them as a list
def getCodeIndexes(code):
   idx = []
   isFound = True
   currIdx = 0
   count = 0
   strLen = len(code)

   while (isFound):
      print ">> searching at " + str(currIdx) + "/" + str(strLen)
      stt = code.find("<code>", currIdx, strLen ) + 6
      stp = code.find("</code>", currIdx, strLen)

      if ( (stt == -1) or (stp == -1) ):
         isFound = False
      else:
         print ("start = " + str(stt) + " stop = " + str(stp) )
         idx.append([stt,stp])
         currIdx = stp + 1
         print "updating currIdx to " + str(currIdx)

      # safegaurd against infinite loops
      if (count > (strLen/2) ):
         isFound = False
      else:
         count = count + 1

   return idx

bot = praw.Reddit(user_agent='arnoldC_GYAAAHH_bot v0.1',
                  client_id='KVEqjgN09CRMaw',
                  client_secret='UBA1Ly9ewZf0M40K4I8q3p7nxoM',
                  username='arnoldC_GYAAAHH_bot',
                  password='spacesNotTabs')

# register for a subreddit
subreddit = bot.subreddit('C_Programming')

# monitor comments
comments = subreddit.stream.comments()

# read thru comments
for comment in comments:
   html_text = comment.body_html
   if checkforcode(html_text):
      printPost(comment)
      # print out the code to show its isolation
      idxs = getCodeIndexes(html_text)
      if ( idxs > 0 ):
         for i in range(len(idxs)):
            pr = idxs[i]
            DBG_WRN('$$$$$$$$$$$' + str(i) + ': ' + str(pr) + '$$$$$$$$' )
            DBG_WRN(html_text[ pr[0] : pr[1] ] )
      #containsBlackList(code)

      print ""
      print ""