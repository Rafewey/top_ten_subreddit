#! usr/bin/env python3
import praw
import pandas
import datetime
import os
import sys

class TopTenSubReddit:
    def __init__(self, subreddit_name, username, password, personal_script, secret, app_name):
        self.subreddit_name = subreddit_name
        self.username = username
        self.password = password
        self.personal_script = personal_script
        self.secret = secret
        self.app_name = app_name

    def get_timestamp(self):
        #Creating a timestamp to add to our file name
        now = datetime.datetime.now()
        fixed_now = now.strftime("%Y%B%d-%I%M%p")
        return fixed_now

    def create_filename(self):
        #Creating our filename
        filename = "{timestamp}_{subreddit}.csv".format(timestamp=self.get_timestamp(), 
        subreddit=self.subreddit_name)
        return filename

    def get_subreddit(self):
        #Accessing the Reddit API
        reddit = praw.Reddit(client_id = self.personal_script, client_secret = self.secret,
        user_agent = self.app_name, username = self.username, password = self.password)
        #Grabbing subreddit
        subreddit = reddit.subreddit(self.subreddit_name)
        #Grabbing only the top 10 posts
        top_subreddit = subreddit.top(limit=10, time_filter="day")
        #Finally, return the var with the stored data
        return top_subreddit

    def parse_subreddit(self):
        #Grabbing subreddit info with get_subreddit method
        subreddit_info = self.get_subreddit()

        #Creating empty dict for subreddit info and appending the info
        topics_dict = {"title":[], "upvotes":[], "author":[]}
        for info in subreddit_info:
            topics_dict["title"].append(info.title)
            topics_dict["upvotes"].append(info.score)
            topics_dict["author"].append(info.author)
        
        #Turning the dictionary into a dataframe with pandas
        topics_data = pandas.DataFrame(topics_dict)

        return topics_data

    def make_spreadsheet(self):
        #Grabbing datafram using parse_subreddit method and creating filename using create_filename method
        dataframe_table = self.parse_subreddit()
        filename = self.create_filename()
        #Finally, making a spreadsheet
        with open(os.path.join(sys.path[0], filename), "w+") as f:
            dataframe_table.to_csv(f, index=False)