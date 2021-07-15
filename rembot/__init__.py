from collections import namedtuple


def consts(**kwargs):
    """ factory function for creating namedtuple from dict """
    return namedtuple(
        'consts',
        list(kwargs.keys()),
        defaults=list(kwargs.values()))()