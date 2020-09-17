#!/usr/bin/python3
"""
titles of the first 10 hot posts listed
"""
import json
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit

    Args:
        subreddit ([str]): [is a subreddit]
    """
    str_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'Chrome/51.0.2704.103'}
    query = requests.get(str_url, headers=header, allow_redirects=False)

    if query.status_code != 200:
        print(None)
    else:
        for title in query.json()['data']['children']:
            print(title['data']['title'])
