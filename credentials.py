import tweepy
from tweepy import OAuthHandler

consumer_key=""
consumer_sugnature=""
access_token=""
access_signaure=""
auth=OAuthHandler(consumer_key, consumer_sugnature)
auth.set_access_token(access_token, access_signaure)

