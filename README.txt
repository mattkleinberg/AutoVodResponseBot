INTRODUCTION
------------

Hello,
This is a simple reddit bot created to answer a very frequent question. That's it lol.
This script uses python 3 and will not work with python 2. It also uses praw and prawoauth2 packages
to access reddit and do its botting.

REQUIREMENTS
------------

1. Python 3.x
2. praw: Python Reddit API Wrapper
3. prawoauth2: moduel to create oauth 2 connection needed to use the reddit api

SETUP
-----

1. If not installed, install praw
    a. pip install praw

2. If not installed, install prawoauth2
    a. pip install prawoauth2

3. Open settings.py and edit the app_key and app_secret with your app_key and app_secret

4. Run onetime.py
    a. This requires a web browser
    b. copy access_token and refresh_token

5. Open settings.py and edit/paste the access_token and refresh_token with the tokens that were printed from running onetime.py

6. Open reddit_bot.py and edit self.question_list to include additional text that will help catch vod questions. Also change self.msg to the appropriate text that you want the bot to respond with.

7. create cron job to reddit_bot.py
    a. * * * * * (cd /path/to/script); ./reddit_bot.py

8. Sit back and drink your drink :P

NOTES
-----

You may see a warning about unclosed <ssl.SSLSocket... when running the script. This is known by praw and can be ignored.
