import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import lex as l

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = "9M3mv6QKuEZN1o74voiZXqHyC"
        consumer_secret = "vygMZiBKxVlTq1iyAkN8q3cBUGMZQWpTLc41xEvBQzR93G5Dtb"
        access_token = "914350353805709312-AX6KU6LGNoxuTGTdck6W7wlQxFT1oue"
        access_token_secret = "dJJ35wMvSRTrhu7UVzcFqPgORgGNXLmIxvsEA21Wqi9HG"

        # attempt authentication
        #try:
            # create OAuthHandler object
        self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
        self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
        self.api = tweepy.API(self.auth)
        #except:
        #print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        rm_ls = r'[0-9]+'
        #return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())
        return ' '.join(re.sub(r'[^\w]' and r'http:\/\/.*[\r\n]*' and r'https?:\/\/.*[\r\n]*' and r'^RT' and rm_ls," ",tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        #analysis = TextBlob(self.clean_tweet(tweet))
	analysis = l.sentiment_main_upd(self.clean_tweet(tweet))
        #  print(tweet)
        #  print (analysis)
        print('\n\n')
        # set sentiment
        if analysis > 0:
            return 'positive'
        elif analysis == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count) #,tweet_mode='extended') #, lang='en', geocode="24.558,77.722,1000km")

            # parsing tweets one by one
            count = 0
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                print("tweet :- ",count)
                print(parsed_tweet['text'])
                count = count+1
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def get_lat(place):
	geolocator=Nominatim()
	location=geolocator.geocode(place)
	print location.latitude, location.longitude
	str_val=""
	str_val=str_val+str(location.latitude)+","+str(location.longitude)  # str() for converting to string
	return str_val


def main(result):
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets

    query =[]
    l.convert_to_dict()
    # tweets = api.get_tweets(query='bjp geocode:24.558,77.722,100km lang:en', count=200)
    ''' inp = raw_input("Enter the query and geocode in the format ( query=' xyz geocode:lattitude,logitude,radius in km (eg 400km) )")
    que = raw_input("Enter the query ")
    inp_loc = raw_input("Enter the name of the place  ")
    inp_range = raw_input("Enter the range in km (eg 100km)")
    str_val=get_lat(inp_loc)  '''
    for key,val in result.iteritems():
         query.append(val)

    que = query[2]
    inp_loc = query[0]
    inp_range = query[1]
    print("query="+que+"loc="+inp_loc+"dist="+inp_range)
    str_val=get_lat(inp_loc)
 
    
    que=que+" -filter:retweets AND -filter:replies"
    que = que+" geocode:"+str_val+","+str(inp_range)+" lang:en" #+ " result_type:recent"

    #inp = inp + ' lang:en'
    tweets = api.get_tweets(query=que, count=200)
    print(tweets)
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % \
        ".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])

    pos = len(ptweets)
    neg = len(ntweets)
    neu = len(tweets) - (len(ptweets) + len(ntweets))

    y = [pos, neu, neg]

    '''display_str = "Sentiment analysis of "+ que + " in "+inp_loc
    plt.title(display_str)
    plt.ylabel('Number of tweets')
    plt.xticks(range( len(y)), ['positive', 'neutral', 'negative'])
    plt.bar(range(len(y)), height=y, width=0.75, align='center', alpha=0.8)
    plt.show();'''
    return y

'''if __name__ == "__main__":
    # calling main function
    main()'''
