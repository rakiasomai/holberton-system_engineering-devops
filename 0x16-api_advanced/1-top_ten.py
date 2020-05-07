#!/usr/bin/python3
'''This module contain the function number_of_subscribers '''

import requests


def top_ten(subreddit):
    ''' def top ten '''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    user = {'user-agent': 'rakia'}
    r = requests.get(url, headers=user)
    if (r.status_code is 404):
        print("None")
    elif 'data' not in r.json():
        print("None")
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
