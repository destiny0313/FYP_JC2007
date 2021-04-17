import tweepy
import csv

    # twitter API credentials of our account

consumer_key = "TGZ1QQwFLRdiZu1JdNPWUYbdg"
consumer_secret = "pEXuKLNsZdHNusRaF7f9JoA1eywDbAKHX3VvIcJXkd6Z819fXo"
access_token = "1296327423244398592-6bOho9V4DYPwFwaPeurjHEmTTiMy3M"
access_token_secret = "jjEPdYvM3bDcbJYZnFUps9qEWomRvqQh19Cm9zRc4TiD2"


with open('//data//opt//users//destiny//real//resource//Stock_List.csv','r') as stocklist:
    with open('//data//opt//users//destiny//real//resource//Tweet.csv','w') as tweetlist:
        
    # prepare file to be written
        
        fields=['Stock','Date','Content','Author','Score','Category']
        tweetwriter = csv.DictWriter(tweetlist, fields)
        tweetwriter.writeheader()
      
    # read stock list csv and skip its title row
        rstocklist = csv.reader(stocklist)
        next(rstocklist)
    
    
    # crawl data for each of the stocks in our list
    
        for row in rstocklist:
            
            tweetsPerQry = 100
            maxTweets = 1000000
            print("Searching for $"+row[0])
            hashtag = "$"+row[0]
            new_search = hashtag + " -filter:retweets"
            
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            
            api = tweepy.API(auth, wait_on_rate_limit=(True))
            
            tweets = tweepy.Cursor(api.search, q=new_search, lang="en", since = "2020-01-01").items()
            
            for tweet in tweets:
                tweetwriter.writerow({'Stock': row[0],'Date': str(tweet.created_at),'Content': tweet.text,'Author': tweet.author.name})
            