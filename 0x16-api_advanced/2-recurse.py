#!/usr/bin/python3
''''This module contain the function number_of_subscribers'''

import requests


def recurse(subreddit, hot_list=[], after=""):
    ''' def recurse '''
    if (after is None):
        return hot_list

    if (len(hot_list) == 0):
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    user = {'user-agent': 'rakia'}

    r = requests.get(url, headers=user)
    if (r.status_code is 404):
        return None
    elif 'data' not in r.json():
        return None
    else:
        r = r.json()
        for y in r['data']['children']:
            hot_list.append(y['data']['title'])

    after = r['data']['after']
    return recurse(subreddit, hot_list, after)
