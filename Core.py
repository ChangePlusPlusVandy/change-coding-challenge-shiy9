# Author: Yuxuan (Bill) Shi
# Vanderbilt University
# Change++ Coding Challenge
# Description (current program): The class can requests 30 quotes each from two endpoints
#                                containing quotes from Donald Trump and Kanye West (endpoint
#                                links in PrivateKey.py file). Randomly choose from a combined 60
#                                quotes and prompt the user to guess whose quote is it. It will
#                                give feedback to the user after the guess is made. It will keep
#                                prompting until the user no longer wishes to play. It will then
#                                end the game and print a game summary.
# Description (original assignment): This class prompts the user of their guess,
#              extracts the Tweets from API, gives out a random tweet, and tells the user if
#              their guess is correct. OAuth operation is performed in this class. Tweets are
#              extracted from API and processed to get rid of all the re-tweets, tags, replies etc.
# Last changed: 9/25/20

'''
---------------------------------------------------------
------NOTE: Please read the README.txt file first!-------
---------------------------------------------------------
'''


import PrivateKey
import random
import requests
import json
# import tweepy  # Twitter API wrapper, here for the Twitter version of the game


class Core(object):
    # Constructor of the class
    def __init__(self):
        self.run_limit = 30  # max quotes from each user
        self.url_1 = PrivateKey.USER_ONE_ENDP  # Endpoint for Donald Trump Quotes
        self.url_2 = PrivateKey.USER_TWO_ENDP  # Endpoint for Kanye West Quotes
        self.user1 = PrivateKey.USER_ONE  # User1 = Donald Trump
        self.user2 = PrivateKey.USER_TWO  # User2 = Kanye West

    def extraction(self, user):
        """
        Extracts quotes from endpoint depending on the subject (Donald Trump or Kanye West)

        :param user: Trump or Kanye--the subject of the quote
        :type user: string constant in PrivateKey.py

        :return: an list (array) of quotes extracted from the end point
        :rtype: list
        """
        url = self.url_1
        keyword = 'message'  # the actual text is under json category "message" for trump endpoint
        all_quotes = []
        if user == self.user2: # if user is Kanye, switch endpoint and keyword variables
            url = self.url_2
            keyword = 'quote'  # the actual text is under "quote" for kanye.rest endpoint

        # Get 30 quotes in this case, each request will return 1 quote.
        # Requesting only 30 since while the trump endpoint is able to return at least 100 quotes,
        #   the kanye.rest endpoint can only return up to 30 before some sort of protection kicks in
        #   and connection is terminated.
        for x in range(self.run_limit):
            r = requests.get(url)
            quote_json = json.loads(r.text)  # json.loads convert json to a dictionary
            quote = str(quote_json[keyword])  # the quote is under the 'keyword' category
            all_quotes.append(quote)  # add to storage list

        return all_quotes

    def quick_str_process(self, str):
        """
        Strips whitespace from both sides of parameter str and turns it to all lowercase

        :param str: string passed in to be processed
        :type str: str

        :return: the processed string
        :rtype: str
        """
        str.strip()
        str = str.lower()

        return str

    def stats_calc(self, tot, cor):
        """
        Calculates the endgame stats and display it to the user. Stats include total number of
        guesses and correct percentage

        :param tot: total number of guesses made
        :type tot: int

        :param cor: total number of correct guesses
        :type cor: int

        :return: None
        """
        cor_perc = cor / tot * 100
        print('You made a total of ' + str(tot) + ' guesses')
        print(str(cor) + ' of them ({:.0f}%) are correct!'.format(cor_perc))

    def ans_valid(self, ans):
        """
        Function is used if user provided unexpected answer (not any form of "Trump" or "Kanye")
        It will keep prompting user until some form of "Trump" or "Kanye" is entered (case
        insensitive)

        :param ans: original answer by the user
        :type ans: str

        :return: an acceptable answer
        :rtype: str
        """
        while ans != 'trump' and ans != 'kanye':
            ans = input('Little typo? Please enter "Trump" or "Kanye": ')
            ans = self.quick_str_process(ans)

        return ans

    def replay_valid(self, rep):
        """
        Similar to ans_valid. This function is used if the user provided unexpected answer
        indicating whether they want to continue playing or not (not any form of "y" or "n")
        It will keep prompting until some form of "y" or "n" is entered

        :param rep: original answer by the user
        :type rep: str

        :return: an acceptable answer
        :rtype: str
        """
        while rep != 'y' and rep != 'n':
            rep = input('Please enter "y" to continue playing, "n" to quit: ')
            rep = self.quick_str_process(rep)

        return rep

    def play(self):
        """
        Function that actually plays the game with the help of other functions. It first loads 30
        quotes each from Donald Trump and Kanye West, places them in separate arrays and merge both
        into one array. A pseudo-random number is generated to pick a quote from the array and the
        quote is displayed to the user. The game will repeat until user enters n to quit.

        :return: None
        """
        print('Getting resources for the game, please wait...\n')
        arr_1 = self.extraction(self.user1)
        arr_2 = self.extraction(self.user2)
        tot_arr = arr_1.copy()  # so arr_1 is not changed
        tot_arr.extend(arr_2)  # merge into one big array
        rg = len(tot_arr)
        tot_guess = 0  # total number of guesses
        cor_guess = 0  # total number of correct guesses

        replay = 'y'
        print('Welcome to Quote guessing game! Here is a quote picked for you: \n')

        while replay == 'y':
            # Since not for crypto purpose, a pseudo-random number will do
            i = random.randint(0, rg - 1)
            cor_ans = 'kanye'  # correct answer for comparison
            disp_ans = 'Kanye'  # correct answer for display
            if i < len(arr_1):
                cor_ans = 'trump'
                disp_ans = 'Trump'

            # Just so the printout is different the second time
            if tot_guess > 0:
                print('Quote this time: \n')

            print(tot_arr[i])  # print the random quote
            ans = input('\nIs it from Donald Trump or Kanye West? Type "Trump" or "Kanye": ')
            tot_guess += 1
            ans = self.quick_str_process(ans)
            if ans != 'trump' and ans != 'kanye':
                ans = self.ans_valid(ans)

            if ans == cor_ans:
                print('\nCongratulations! You are correct, it is from', disp_ans)
                cor_guess += 1
            else:
                print('Good try! It is actually from', disp_ans)

            print()
            replay = input('Would you like to play again? Type "y" for yes or "n" for no')
            replay = self.quick_str_process(replay)
            if replay != 'y' and replay != 'n':
                replay = self.replay_valid(replay)

        print('Thanks for playing! Here are some stats: ')
        self.stats_calc(tot_guess, cor_guess)


''' The Twitter API part of the assignment
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
        tweets_stats.append(new_comers)

        # Update the oldest tweet id - 1 to extract older tweets, until 3200
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
        tot_arr = elon_arr.copy()
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
            ans = input('Is it from Elon Must or Kanye West? Type "Elon" or "Kanye"')
            ans.strip()
            ans = ans.lower()

            if ans == cor_ans:
                print('Congratulations, you are correct, it is from', cor_ans)
            else:
                print('Good try, it is actually from', cor_ans)

            replay = input('Would you like to play again? Type "y" or "n"')
            replay.strip()
            replay = replay.lower()       '''

