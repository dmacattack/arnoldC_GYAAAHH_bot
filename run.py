import praw

# https://github.com/praw-dev/praw/

   
# check for code in the post
def checkforcode(text):
   if "#define" in text:
      return True
   else:
      return False
   
# print the post
def printPost(author, text):
   print "---------------------------"
   print "author: %s" %author
   print " text: %s" % text
   print "---------------------------"

bot = praw.Reddit(user_agent='arnoldC_GYAAAHH_bot v0.1',
                  client_id='KVEqjgN09CRMaw',
                  client_secret='UBA1Ly9ewZf0M40K4I8q3p7nxoM',
                  username='arnoldC_GYAAAHH_bot',
                  password='spacesNotTabs')

# register for a subreddit
subreddit = bot.subreddit('ProgrammerHumor')

# monitor comments
comments = subreddit.stream.comments()

# read thru comments
for comment in comments:
   text = comment.body
   author = comment.author
   if checkforcode(text):
      printPost(author, text)
      
