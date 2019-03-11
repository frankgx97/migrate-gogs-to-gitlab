#coding: utf8
from providers.gitlab import GitlabInstance
from providers.gogs import GogsInstance

gogs_token = 'token'

gogs = GogsInstance('https://your.gogs.instance/', gogs_token)
gitlab = GitlabInstance('https://your.gitlab.instance/','token')

def migrate_repos(gogs, gitlab):
    gogs_repo_list = gogs.list_repos()

    gogs_repo_url_list = []

    for i in gogs_repo_list:
        gogs_repo_url_list.append({
            "name":i['full_name'],
            "desc":i['description']
            })
    repo_list = gogs_repo_url_list

    name_checkduplicate = []
    for i in reversed(repo_list):
        name = i['name'].split('/')[1]
        if name not in name_checkduplicate:
            name_checkduplicate.append(name)
        else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!duplicate')
        desc = i['desc']
        url = 'https://'+gogs_token+'@your.gogs.instance/'+i['name']
        print(name, desc, url)
        print(gitlab.create(name, desc, url))
        print('=====================================')

migrate_repos(gogs, gitlab)