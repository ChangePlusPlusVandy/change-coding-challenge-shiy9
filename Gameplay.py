# Author: Yuxuan (Bill) Shi
# Vanderbilt University
# Change++ Coding Challenge
# Last Changed: 9/23/20

import PrivateKey
import tweepy

def main():
    # Twitter OAuth, set access tokens and keys
    auth = tweepy.OAuthHandler(PrivateKey.TWT_API_KEY, PrivateKey.TWT_API_SECRET)
    auth.set_access_token(PrivateKey.TWT_TKN, PrivateKey.TWT_TKN_SECRET)

    # Create API instance
    api = tweepy.API(auth)
    # public_tweet = api.home_timeline()
    # for tweet in public_tweet:
    #     print(tweet.text)

    str = 'Elon says: http:// what the? http://what_is_ths'
    str_list = str.split()
    str_list = [str for str in str_list if ('http://' not in str)]
    str_list = " ".join(str_list)
    print(str_list)



if __name__ == '__main__':
    main()
