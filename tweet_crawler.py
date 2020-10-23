import tweepy
import mysql.connector as mc



mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "FYP"
    )

mycursor = mydb.cursor()
sql_insert = "INSERT IGNORE INTO tweet (Stock_Code, Authur, Content, Date) VALUES (%s, %s, %s, %s);"
sql_read = "Select * FROM stock_list;"

# Get stock list
mycursor.execute(sql_read);
stocklist = mycursor.fetchall()

# Twitter API credential
consumer_key = "TGZ1QQwFLRdiZu1JdNPWUYbdg"
consumer_secret = "pEXuKLNsZdHNusRaF7f9JoA1eywDbAKHX3VvIcJXkd6Z819fXo"
access_token = "1296327423244398592-6bOho9V4DYPwFwaPeurjHEmTTiMy3M"
access_token_secret = "jjEPdYvM3bDcbJYZnFUps9qEWomRvqQh19Cm9zRc4TiD2"

for x in stocklist:
    tweetsPerQry = 100
    maxTweets = 1000000
    print("$"+x[0])
    hashtag = "$"+x[0]
    new_search = hashtag + " -filter:retweets"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=(True))

    tweets = tweepy.Cursor(api.search, q=new_search, lang="en", result_type="recent").items(5)

    for tweet in tweets:
        mycursor.execute(sql_insert,(x[0],tweet.author.name,tweet.text,str(tweet.created_at)))
        mydb.commit()
        
mycursor.close()
