#!/usr/bin/python3
'''Recurse it'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''returns a list containing the titles of all hot articles'''

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    url_pagination = url + after
    header = {'User-Agent': 'holberton'}

    response = requests.get(url_pagination,
                            headers=header,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        first_level = data.get('children')

        for post_info in first_level:
            hot_list.append(post_info.get('data').get('title'))

        if data.get('after'):
            after = "?after=" + data.get('after')
            return recurse(subreddit, hot_list, after)

        else:
            return (hot_list)
