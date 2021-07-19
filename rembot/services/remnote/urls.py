CREATE = 'https://api.remnote.io/api/v0/create'
GET = 'https://api.remnote.io/api/v0/get'
GET_BY_NAME = 'https://api.remnote.io/api/v0/get_by_name'
DOC = 'https://www.remnote.io/document/'


def doc_url(rem_id):
    return DOC + rem_id


def rem_id_from_url(url):
    return url.split('/')[-1]
