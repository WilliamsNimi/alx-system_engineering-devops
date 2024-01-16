#!/usr/bin/python3
""" Fetching data from the Reddit API """


import requests
import sys

def recurse(subreddit, hot_list=[]):
    """ Top 10 titles in Subreddits recursive"""
    red_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":"new_user"}
    params = {"after": "after"}
    response = requests.get(red_url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        content = response.json().get('data').get('children')
        content2 = response.json().get('data').get('after')
        titles = list(map(lambda x: x.get('data').get('title'), content))
        hot_list.extend(titles)
        if content2 is None:
            return hot_list
        return recurse(subreddit, hot_list)
    else:
        print(None)

if __name__ == "__main__":
    recurse(sys.argv[1])
