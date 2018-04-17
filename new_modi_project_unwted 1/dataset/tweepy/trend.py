
import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "IfuKYq60y957g3BgofJbYrHUz"
consumer_secret = "lWAiJ9rTNvVMSjNJymiAqrZX4CsZouL8ZTWdWxPDzJThTL2iBz"
access_key = "948230321660502017-SWKah1yrR5R5z0b5COfqTZXTqIKJh6Q"
access_secret = "zBUj0kX4WsWHNbiKEYxGi62zvzyWd2aXKeHoXDPvNd3Cg"


def get_all_tweets():
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	api = tweepy.API(auth)

        trends1 = api.trends_place(1) # from the end of your code 
                                      # trends1 is a list with only one element in it, which is a 
                                      # dict which we'll put in data.
        data = trends1[0] 
                                      # grab the trends
        trends = data['trends']
                                      # grab the name from each trend
        #names = [trend['name'] for trend in trends]
                                      # put all the names together with a ' ' separating them
        #trendsName = ' '.join(names)
        for trend in trends:
             print(trend['name']+'\n')


if __name__ == '__main__':
	#pass in the username of the account you want to download
    #search_key = raw_input("Enter the name :  ")
    get_all_tweets()	
    #get_all_tweets("@narendramodi")
    
    
    
    
    
    
    
    
    
    
