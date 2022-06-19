from imports import*
from funcs import *

def new_post(datetimetext, picture):

    title = submission.title
    image = InlineImage(path="post.png")
    selftext = "{image1}"
    media = {"image1": image}
    
    # create db if ones not made
    conn = sqlite3.connect('pictures.db')

    c = conn.cursor()
 
    # insert
    try:
        c.execute("INSERT INTO pictures VALUES (?, ?, ?)", (None, datetimetext, picture))

    except Exception as e:
        print(f'Inserting into database failed - https://reddit.com{submission.permalink}')
        pass
    
    else:
        try:
            #This will try to update the post to twitter
            api.update_status_with_media(f'#{submission.subreddit}', filename) #Add as many #'s as you want
        except Exception as e:
            print(f'Posting to Twitter failed from https://reddit.com{submission.permalink}')
            pass
        else:
            print(f'Posted to Twitter from {submission.subreddit} <3')

    #commit the action
    conn.commit()

    #close db after action
    conn.close()

# assign the values accordingly - YOU WILL NEED ELEVATED ACCESS for the Twitter Api, it's automatic approval from https://developer.twitter.com/en/portal/dashboard
# Remember to enable v1.0 permissions for posting in your User authentication settings
# OAuth 1.0a NEEDS TO BE ENABLED
# Then get your keys!
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
user_name = "" #Your @username

#Create you reddit API application! https://ssl.reddit.com/prefs/apps/
# Then link your settings here 
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    username='', # Reddit username
    password='', # Reddit password, needs to be an account registered with a password
    user_agent='') #Application name you made

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

print("LET THEIR BE PICTURES")
#Add as many subreddits as you want, each seperated by + 
for submission in reddit.subreddit("memes+ComedyCemetery+dankmemes").stream.submissions(skip_existing=True):
    try:
        def download_image(post):
            request = url.Request(post)
            img = url.urlopen(request).read()
            with open (file_name + '.png', 'wb') as f: f.write(img)

        post = submission.url
        file_name = ('post')
        download_image(post)

        # the path of the media to be uploaded
        filename = "post.png"

        with open(filename, "rb") as img_file:
            my_string = base64.b64encode(img_file.read())

        datetimetext2 = datetime.now().strftime("%B %d, %Y %I:%M%p")

    except Exception as e:
        print(e)
        pass

    else:
        new_post(datetimetext2, my_string)