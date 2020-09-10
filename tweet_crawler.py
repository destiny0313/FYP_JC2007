import tweepy

# Twitter API credential
consumer_key = "TGZ1QQwFLRdiZu1JdNPWUYbdg"
consumer_secret = "pEXuKLNsZdHNusRaF7f9JoA1eywDbAKHX3VvIcJXkd6Z819fXo"
access_token = "1296327423244398592-6bOho9V4DYPwFwaPeurjHEmTTiMy3M"
access_token_secret = "jjEPdYvM3bDcbJYZnFUps9qEWomRvqQh19Cm9zRc4TiD2"

tweetsPerQry = 100
maxTweets = 1000000
hashtag = "$TSLA"
new_search = hashtag + " -filter:retweets"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search, q=new_search, lang="en", result_type="recent").items(5)

for tweet in tweets:
    print(str(tweet.created_at))
    print(tweet.author.name)
    print(tweet.text+"\n")