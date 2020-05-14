#! usr/bin/env python3
import praw
import pandas
import datetime

class TopTenSubReddit:
    def __init__(self, subreddit_name, username, password, personal_script, secret, app_name):
        self.subreddit_name = subreddit_name
        self.username = username
        self.password = password
        self.personal_script = personal_script
        self.secret = secret
        self.app_name = app_name

    def get_subreddit(self):
        #Accessing the Reddit API
        reddit = praw.Reddit(client_id = self.personal_script, client_secret = self.secret,
        user_agent = self.app_name, username = self.username, password = self.password)
        #Grabbing subreddit
        subreddit = reddit.subreddit(self.subreddit_name)