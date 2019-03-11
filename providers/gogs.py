#coding:utf8
import requests
import json

from .instance import Instance

class GogsInstance(Instance):
    prefix = 'api/v1'

    def list_repos(self):
        r = requests.get(
            self.api_url + '/user/repos',
            headers={"Authorization": "token {}".format(self.token)}
            )
        return json.loads(r.text)