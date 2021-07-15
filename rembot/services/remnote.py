import os
import requests

from rembot import consts


REMNOTE_API_KEY = os.environ['REMNOTE_API_KEY']
REMNOTE_USER_ID = os.environ['REMNOTE_USER_ID']

urls = consts(
    CREATE='https://api.remnote.io/api/v0/create',
    GET='https://api.remnote.io/api/v0/get',
    GET_BY_NAME='https://api.remnote.io/api/v0/get_by_name',
    DOC='https://www.remnote.io/document/')


def doc_url(rem_id):
    return urls.DOC + rem_id


def rem_id_from_url(url):
    return url.split('/')[-1]


async def enable(app):
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
    return doc_url(response_data['remId'])


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
