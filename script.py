from toptensubreddit import TopTenSubReddit
import time

print("IN ORDER TO GRAB THE TOP 10 POSTS FROM YOUR DESIERED SUBREDDIT, YOU MUST FIRST HAVE THE CORRECT CREDENTIALS")

user_username = input("YOUR REDDIT USERNAME")
user_password = input("YOUR REDDIT PASSWORD")
user_app_name = input("YOUR APP NAME")
user_personal_use_script = input("YOUR PERSONAL SCRIPT KEY")
user_secret = input("YOUR SECRET KEY")
user_subreddit = input("WHAT SUBREDDIT WOULD YOU LIKE TO SCRAPE FROM?")

#remove any whitespaces from the left and right of the strings that were inputted
user_username.strip()
user_password.strip()
user_app_name.strip()
user_personal_use_script.strip()
user_secret.strip()

#login to reddit with appropiate credentials
login = TopTenSubReddit(user_subreddit, user_username, user_password, user_personal_use_script,
user_secret, user_app_name)

while True:
    login.make_spreadsheet()
    time.sleep(3600)