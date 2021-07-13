import os
import requests


REMNOTE_API_URL_CREATE = 'https://api.remnote.io/api/v0/create'
REMNOTE_DOC_URL = 'https://www.remnote.io/document/'
REMNOTE_API_KEY = os.environ['REMNOTE_API_KEY']
REMNOTE_USER_ID = os.environ['REMNOTE_USER_ID']


def attach(app):
    pass

def create_rem(parent, text):
    print('createt_rem')
    request_data = dict(
        apiKey=REMNOTE_API_KEY,
        userId=REMNOTE_USER_ID,
        parentId=parent,
        text=text,
        positionAmongstSiblings=0)
    response = requests.post(REMNOTE_API_URL_CREATE, data=request_data)
    response_data = response.json()
    return REMNOTE_DOC_URL + response_data['remId']
