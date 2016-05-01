import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

consumer_key=""
consumer_secret=""
access_token=""
access_secret=""
auth= OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api=tweepy.API(auth)
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class start_survillance(StreamListener):
 
    def on_data(self, data):
        try:
            with open('stream.json', 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, start_survillance())
twitter_stream.filter(track=['#VIEWS'])

if __name__ == '__main__':
    start_survillance().on_data()
    start_survillance().on_error()

