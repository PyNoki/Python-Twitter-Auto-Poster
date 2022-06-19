# Twitter-Auto-Poster
This utilizes PRAW and TWEEPY to create a bot that keeps posting everytime a new post in a subreddit gets uploaded, without posting idential dupes too!

# Requirements
- A twitter account with developer access, and elevated permissions
- A reddit account 
- pip install Pillow
- pip install praw
- pip install tweepy
- You may need more, just install as needed

# Setup
- Create your twitter app here https://developer.twitter.com/en/portal/dashboard
- Remember to enable v1.0 permissions for posting in your User authentication settings - OAuth 1.0a NEEDS TO BE ENABLED for your twitter app
- Create you reddit API application! https://ssl.reddit.com/prefs/apps/

# Using
- Run main.py, you may need to do "python main.py" or "python3 main.py" depending

# Purpose
- This will post EVERY new submission from all of the subreddits that you've assigned, this will not upload duplicate images!
- Keep you and your followers supplied with whatever you choose
- Creating a stream for your discord / twitter / any application you choose to make webhooks
