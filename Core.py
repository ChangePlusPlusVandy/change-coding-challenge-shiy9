# Author: Yuxuan (Bill) Shi
# Vanderbilt University
# Change++ Coding Challenge
# Description: (Please read the README.txt file first.) This class prompts the user of their guess,
#              extracts the Tweets from API, gives out a random tweet, and tells the user if
#              their guess is correct. OAuth operation is performed in this class. Tweets are
#              extracted from API and processed to get rid of all the re-tweets, tags, replies etc.


import PrivateKey
import tweepy
import random
import requests
import json


class Core(object):
    def __init__(self):
        self.run_limit = 5  # max quotes from each user
        self.url_1 = PrivateKey.USER_ONE_ENDP
        self.url_2 = PrivateKey.USER_TWO_ENDP
        self.user1 = PrivateKey.USER_ONE  # User1 = Donald Trump
        self.user2 = PrivateKey.USER_TWO  # User2 = Kanye West

    def extraction(self, user):
        url = self.url_1
        keyword = 'message'
        all_quotes = []
        if user == self.user2:
            url = self.url_2
            keyword = 'quote'

        for x in range(self.run_limit):
            r = requests.get(url)
            quote_json = json.loads(r.text)
            quote = str(quote_json[keyword])
            all_quotes.append(quote)

        return all_quotes

    # Randomly picks a tweet and returns it
    def play(self):
        print('Getting resources for the game, please wait...')
        arr_1 = self.extraction(self.user1)
        arr_2 = self.extraction(self.user2)
        tot_arr = arr_1
        tot_arr.extend(arr_2)
        rg = len(tot_arr)

        replay = 'y'

        while replay == 'y':
            # Since not for crypto purpose, a pseudo-random number will do
            i = random.randint(0, rg)
            cor_ans = 'kanye'
            if i < len(arr_1):
                cor_ans = 'trump'

            print('Welcome to Tweet guessing game, here is a tweet picked for you: ')
            print(tot_arr[i])
            ans = input('Is it from Donald Trump or Kanye West? Type \"Trump\" or \"Kanye\"')
            ans.strip()
            ans = ans.lower()

            if ans == cor_ans:
                print('Congratulations, you are correct, it is from', cor_ans)
            else:
                print('Good try, it is actually from', cor_ans)

            replay = input('Would you like to play again? Type \"y\" or \"n\"')
            replay.strip()
            replay = replay.lower()

'''
class Core(object):
    def __init__(self):
        # Twitter OAuth, set access tokens and keys
        auth = tweepy.OAuthHandler(PrivateKey.TWT_API_KEY, PrivateKey.TWT_API_SECRET)
        auth.set_access_token(PrivateKey.TWT_TKN, PrivateKey.TWT_TKN_SECRET)
        self.api = tweepy.API(auth)
        self.run_limit = 200  # max out the user_timeline return
        self.user_one = 'elonmusk'
        self.user_two = 'kanyewest'

    # Extract the tweets of one user without any replies/tags/retweets.
    def extraction(self, userName):
        # print('Getting resources for the game, please wait...')
        # Note: excluding retweets and replies and tags will not extract 3200 tweets
        #       The above three categories still count towards the 3200 total count
        tweets_stats = []  # Array to hold all the tweets in "Status" object format
        tweets = []  # Array to hold all the tweet text

        # Do the initial loading and start the loop
        new_comers = self.api.user_timeline(screen_name=userName, tweet_mode='extended',
                                            include_rts=False, exclude_replies=True,
                                            count=self.run_limit)

        # Append Status objects to array
        # Do not convert to text and store in array yet
        tweets_stats.extend(new_comers)

        # Update the oldest tweet id - 1 to extract all 3200
        old_id = tweets_stats[-1].id - 1

        # Extraction and process here
        while len(new_comers) > 1:
            # New set of 200 tweets, does not include replies or retweets (together with tags)
            new_comers = self.api.user_timeline(screen_name=userName, tweet_mode='extended',
                                                include_rts=False, exclude_replies=True,
                                                count=self.run_limit, max_id=old_id)
            tweets_stats.extend(new_comers)
            old_id = tweets_stats[-1].id - 1

        # Get rid of the links in the tweet
        for stat in tweets_stats:
            temp_str = stat.full_text
            str_list = temp_str.split()
            str_list = [str for str in str_list if ('http://' not in str)]
            str_list = " ".join(str_list)
            tweets.append(str_list)

        return tweets

    # Randomly picks a tweet and returns it
    def play(self):
        print('Getting resources for the game, please wait...')
        elon_arr = self.extraction(self.user_one)
        kanye_arr = self.extraction(self.user_two)
        tot_arr = elon_arr
        tot_arr.append(kanye_arr)
        range = len(tot_arr)

        replay = 'y'

        while replay == 'y':
            # Since not for crypto purpose, a pseudo-random number will do
            i = random.randint(0, range)
            cor_ans = 'kanye'
            if i < len(elon_arr):
                cor_ans = 'elon'

            print('Welcome to Tweet guessing game, here is a tweet picked for you: ')
            print(tot_arr[i])
            ans = input('Is it from Elon Must or Kanye West? Type \"Elon\" or \"Kanye\"')
            ans.strip()
            ans = ans.lower()

            if ans == cor_ans:
                print('Congratulations, you are correct, it is from', cor_ans)
            else:
                print('Good try, it is actually from', cor_ans)

            replay = input('Would you like to play again? Type \"y\" or \"n\"')
            replay.strip()
            replay = replay.lower()       '''

