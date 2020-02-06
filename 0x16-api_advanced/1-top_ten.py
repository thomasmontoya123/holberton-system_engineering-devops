#!/usr/bin/python3
'''Top ten posts'''
import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts'''
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    header = {'User-Agent': 'holberton'}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        first_level = response.json().get('data').get('children')
        for post_info in first_level:
            print(post_info.get('data').get('title'))

    else:
        print(None)
