import os
import requests

from rembot import consts
from rembot.services.remnote import urls


REMNOTE_API_KEY = os.environ['REMNOTE_API_KEY']
REMNOTE_USER_ID = os.environ['REMNOTE_USER_ID']


async def enable(events):
    pass


async def create(parent, text):
    request_data = dict(
        apiKey=REMNOTE_API_KEY,
        userId=REMNOTE_USER_ID,
        parentId=parent,
        text=text,
        positionAmongstSiblings=0)
    response = requests.post(urls.CREATE, data=request_data)
    response_data = response.json()
    return urls.doc_url(response_data['remId'])


async def get(rem_id):
    request_data = dict(
        apiKey=REMNOTE_API_KEY,
        userId=REMNOTE_USER_ID,
        remId=rem_id)
    response = requests.post(urls.GET, data=request_data)
    response_data = response.json()
    return response_data


async def get_by_name(name):
    request_data = dict(
        apiKey=REMNOTE_API_KEY,
        userId=REMNOTE_USER_ID,
        name=name)
    response = requests.post(urls.GET_BY_NAME, data=request_data)
    response_data = response.json()
    return response_data
