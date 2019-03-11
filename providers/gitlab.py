#coding:utf8
import requests
import json
from .instance import Instance

class GitlabInstance(Instance):
    prefix = 'api/v4'

    def create(self, name, description, url):
        data = {
            "name": name,
            "description": description,
            "visibility": 'private',
            "import_url": url,
        }
        r = requests.post(
            self.api_url + '/projects',
            headers={"Private-Token": self.token},
            data=data
        )
        return json.loads(r.text)

