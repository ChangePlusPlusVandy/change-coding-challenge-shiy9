Hello!

A couple of things I want to mention before the program is reviewed. 

1. I am in China at the moment and cannot access Twitter API even when using a VPN. I could open
   Twitter's webpage but cannot connect to the API with "connection failed, connected party did 
   not respond" errors. I still wrote code for the Twitter API solely based on what I "think" how
   the program should work since I cannot test the program. The code is commented out at the end of
   Core.py. I emailed Ethan, and he gave me two endpoints--one for quotes from Trump, one for quotes
   from Kanye--to work with as an alternative option. That project is currently working, and the
   Twitter API part is commented out just to show that I tried it (as instructed by Ethan).

2. I am most familiar with C++. However, I struggled a lot to find a useable HTTP request library
   for C++ (this is before I found out I cannot connect to Twitter API). I tried a library 
   called twitcurl which seemed like a Twitter API wrapper, but the project required Visual C++ 
   2010 edition to build. I am unable to download that version from Microsoft's website since the
   link didn't work for some reason. Another library I tried was libcurl which is just a generic
   http request library. However, I found very limited documentation on how to actually use the 
   library to make requests. 
   
   I finally decided to switch to Python to do this project, and it was indeed a lot easier than 
   C++ to implement the HTTP requests. I learned Python myself over the summer and definitely is
   not as fluent with it as with C++. Some usage of certain things may not be the "best practice" 
   so feel free to point them out! 
   
3. The project is written in Pycharm IDE, and Gameplay.py is the main program to run. Virtual
   environment (venv) containing all the libraries is included in the GitHub repo. The only 
   library I needed to install was the "tweepy" library--a Twitter API wrapper. But again it
   technically was not used since all the code related it is commented out. Other libraries such 
   as json and requests were installed along with Python itself. If for some reason the project
   fails to run in other IDEs such as Spyder (I am not sure since I do not have Spyder installed),
   please download Pycharm to run the project, it is free! Sorry for any potential inconvenience.
 
4. This alternative version of the game only has 60 quotes--30 from Trump and 30 from Kanye. 
   Although I am able to extract 100 quotes from the Trump endpoint (did not try more since the 
   100 already took 6 minutes), I was only able to pull 30 quotes from Kanye endpoint before some
   sort of protection from the endpoint kicks in and terminated the connection. For the fairness
   of the game, I only opted to pull 30 quotes from Trump's endpoint as well.
   
5. The code does work but sometimes I would run into connection issues after frequently requesting
   from kanye.rest endpoint. It would allow me to pull again after a few minutes of wait time. I
   am not sure if it is because I am accessing the endpoint from a foreign IP. If it happens again
   during the review process. Please wait a couple minutes before requesting again. Hopefully a US
   IP can avoid such issue. 
   
   
   Thank you very much for reading this through!
   
   
Bill
