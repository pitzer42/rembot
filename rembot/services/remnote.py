import os
import requests
from collections import namedtuple


REMNOTE_API_URL_CREATE = 'https://api.remnote.io/api/v0/create'
REMNOTE_API_URL_GET = 'https://api.remnote.io/api/v0/get'
REMNOTE_API_URL_GET_BY_NAME = 'https://api.remnote.io/api/v0/get_by_name'
REMNOTE_DOC_URL = 'https://www.remnote.io/document/'
REMNOTE_API_KEY = os.environ['REMNOTE_API_KEY']
REMNOTE_USER_ID = os.environ['REMNOTE_USER_ID']


# Rem = namedtuple('Rem', '_id, parent, children, name')

async def attach(app):
    pass


async def create(parent, text):
    request_data = dict(
        apiKey=REMNOTE_API_KEY,
        userId=REMNOTE_USER_ID,
        parentId=parent,
        text=text,
        positionAmongstSiblings=0)
    response = requests.post(REMNOTE_API_URL_CREATE, data=request_data)
    response_data = response.json()
    return REMNOTE_DOC_URL + response_data['remId']


def parse_rem_id_from_url(url):
    return url.split('/')[-1]


async def get_by_name(name):
    request_data = dict(
        apiKey=REMNOTE_API_KEY,
        userId=REMNOTE_USER_ID,
        name=name)
    response = requests.post(REMNOTE_API_URL_GET_BY_NAME, data=request_data)
    response_data = response.json()
    return response_data


async def get(rem_id):
    request_data = dict(
        apiKey=REMNOTE_API_KEY,
        userId=REMNOTE_USER_ID,
        remId=rem_id)
    response = requests.post(REMNOTE_API_URL_GET, data=request_data)
    response_data = response.json()
    return response_data
