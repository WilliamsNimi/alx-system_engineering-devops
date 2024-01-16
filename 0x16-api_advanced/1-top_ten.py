#!/usr/bin/python3
""" Fetching data from the Reddit API """


import requests
import sys

def top_ten(subreddit):
    """ Top 10 titles in Subreddits"""
    red_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":"new_user"}
    params = {"limit":10}
    response = requests.get(red_url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        content = response.json().get('data').get('children')
        titles = list(map(lambda x: x.get('data').get('title'), content))
        for title in titles:
            print(title)
    else:
        print(None)

if __name__ == "__main__":
    top_ten(sys.argv[1])
