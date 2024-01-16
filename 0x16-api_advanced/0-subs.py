#!/usr/bin/python3
""" Fetching data from the Reddit API """


import json
import sys
import urllib.request

def number_of_subscribers(subreddit):
    """Number of subscribers in a subreddit"""
    red_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    with urllib.request.urlopen(red_url) as response:
        json_file = json.loads(response.read())
        if response.status == 200:
            return json_file['data']['subscribers']
    return 0

if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
