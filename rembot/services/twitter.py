import os
import json
import requests

TWITTER_BEARER_TOKEN = os.environ['TWITTER_BEARER_TOKEN']

_headers = dict(
    Authorization=f'Bearer {TWITTER_BEARER_TOKEN}'
)


async def enable(events):
    pass


def get_user_id(username):
    url = f'https://api.twitter.com/2/users/by?usernames={username}'
    response = requests.get(url, headers=_headers).json()
    return response['data'][0]['id']


def get_tweets_from(user_id, since=None):
    url = f'https://api.twitter.com/2/users/{user_id}/tweets?tweet.fields=created_at&expansions=author_id&user.fields=created_at&max_results=5'
    if since:
        url += f'&since_id={since}'
    return requests.get(url, headers=_headers).json().get('data')


def get_favorites_from(user_id, since=None):
    url = f'https://api.twitter.com/1.1/favorites/list.json?user_id={user_id}'
    if since:
        url += f'&since_id={since}'
    return requests.get(url, headers=_headers).json()


def get_tweet_url_from_favorites(favs):
    return [fav['entities']['urls'][0]['url'] for fav in favs]