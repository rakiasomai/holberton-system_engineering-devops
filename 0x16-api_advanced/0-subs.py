#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    ''' def number of subscribers'''
    get_url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'philsrequest'}
    y = requests.get(get_url, headers=headers)
    if (y.status_code is 404 or y.status_code is 302):
        return 0
    y = y.json()
    if ('error' in y):
        return 0
    elif ('subscribers' in y['data']):
        return y['data']['subscribers']
    else:
        return 0
