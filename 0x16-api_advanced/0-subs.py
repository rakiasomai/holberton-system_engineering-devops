#!/usr/bin/python3
''' This module contain the function number_of_subscribers '''

import requests


def number_of_subscribers(subreddit):
    ''' def number of subscribers '''
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    user = {'user-agent': 'rakia'}
    r = requests.get(url, headers=user)
    if (r.status_code is 302 or r.status_code is 404):
        return 0
    r = r.json()
    if ('error' in r):
        return 0
    elif ('subscribers' in r['data']):
        return r['data']['subscribers']
    else:
        return 0
