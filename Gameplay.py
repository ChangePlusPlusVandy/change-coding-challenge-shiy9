# Author: Yuxuan (Bill) Shi
# Vanderbilt University
# Change++ Coding Challenge
# Last Changed: 9/23/20

import PrivateKey
import tweepy
import requests
import json
import Core


def main():
    test = Core.Core()
    Core.Core.play(test)



    # potus_arr = []
    # for x in range(30):
    #     # url = 'https://api.whatdoestrumpthink.com/api/v1/quotes/random'
    #     url = 'https://api.kanye.rest'
    #     r = requests.get(url)
    #     # print(r.text)
    #     quote_json = json.loads(r.text)
    #     # print(quote_json)
    #     # quote = str(quote_json['message'])
    #     quote = str(quote_json['quote'])
    #     potus_arr.append(quote)
    #
    #
    # print(potus_arr[0])


    # Twitter OAuth, set access tokens and keys
    # auth = tweepy.OAuthHandler(PrivateKey.TWT_API_KEY, PrivateKey.TWT_API_SECRET)
    # auth.set_access_token(PrivateKey.TWT_TKN, PrivateKey.TWT_TKN_SECRET)

    # Create API instance
    # api = tweepy.API(auth)
    # public_tweet = api.home_timeline()
    # for tweet in public_tweet:
    #     print(tweet.text)




if __name__ == '__main__':
    main()
