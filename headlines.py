import requests
""" Gets headlines of current events
    from user desired sources.
"""

###
API = '2010256b6ea94d07be79a83ef4b49669'
URL = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&''apiKey=2010256b6ea94d07be79a83ef4b49669'
###

class headlines:
    param = {}

    def __init__(self):
        self.param['apiKey'] = API
        self.param['language'] = 'en'

