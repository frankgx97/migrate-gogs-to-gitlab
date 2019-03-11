#coding:utf8

class Instance:
    token = ''
    url = ''
    prefix = ''
    api_url = ''

    def __init__(self, url, token):
        self.token = token
        self.instance_url = url
        self.api_url = self.instance_url + self.prefix
        return