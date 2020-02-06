#!/usr/bin/python3
'''How many subs'''
import requests


def number_of_subscribers(subreddit):
    '''return the number of subscribers'''
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    header = {'User-Agent': 'holberton'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return (0)
