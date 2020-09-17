#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should
return 0.
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    Get all users of a subreddit

    Args:
        subreddit ([str]): [is a subreddit]

    Returns:
        [int]: [number of subcriptors]
    """
    str_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Chrome/51.0.2704.103'}
    query = requests.get(str_url, headers=header, allow_redirects=False)

    if query.status_code == 200:
        return query.json()['data']['subscribers']
    return 0
