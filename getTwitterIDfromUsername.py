#! python3

from keysAuthentication import *

import tweepy

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# api.get_user(put id here )
# http://docs.tweepy.org/en/v3.5.0/api.html?highlight=get_user#user-methods

with open("usernames.txt", "r") as txtFile:
    # listOfNames = txtFile.readlin()
    for name in txtFile:
        # print(name.rstrip("\n"))
        print(name[:-2])