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


def getCode(html):
   # TODO substring the text
   codeStart = html.find("<code>")
   codeStop  = html.find("</code>")
   code = html[codeStart+6:codeStop]
   return code

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
      code = getCode(comment.body_html)
      #containsBlackList(code)
      DBG_WRN(code)
      print ""
      print ""

