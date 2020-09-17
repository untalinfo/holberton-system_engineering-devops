#!/usr/bin/python3
"""
titles of the first 10 hot posts listed
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles for a
    given subreddit

    Args:
        subreddit ([str]): [is a subreddit]
        hot_list (list, optional): [list of titles]. Defaults to [].
        after ([type], optional): [netx page]. Defaults to None.
    """
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Chrome/51.0.2704.103'}
    QUERY = requests.get(URL, headers=header, allow_redirects=False,
                         params={'after': after})
    if QUERY.status_code != 200:
        print(None)
    else:
        after = QUERY.json()['data']['after']
        if after is None:
            return hot_list
        for post in QUERY.json()['data']['children']:
            hot_list.append(post['data']['title'])
        return recurse(subreddit, hot_list, after)
