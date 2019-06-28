import praw
from config import botname, password, subs, c_id, c_secret

# api login
reddit = praw.Reddit(client_id=c_id,
                    client_secret=c_secret,
                    username=botname,
                    password=password,
                    user_agent='a bot that provides a link')
print('logged in')

# active subredditss
subreddits = reddit.subreddit(subs)
print('sub selected')

# phrase to activate bot and link to return
keyphrase = 'link?'
imgur_link = '[link](https://imgur.com/vGRpyq8)'

print('searching comments...')
# loop through comment stream to find keyphrase and reply
for comment in subreddits.stream.comments():
    if keyphrase in comment.body:
        try:
            comment.reply(imgur_link)
            print("link posted")
            print('searching comments...')
        except:
            print("post failed")
            print('searching comments...')
