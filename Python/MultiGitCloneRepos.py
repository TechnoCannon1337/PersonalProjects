import json
import os
import requests

def multiCloneGitHubUserRepos(gitHubTargetUser, pageCount='1000'):
    baseURL = 'https://api.github.com/users/'
    pageQuery ='/repos?per_page='
    gitHubRequest=requests.get(baseURL + gitHubTargetUser + pageQuery + pageCount)
    contents = json.loads(gitHubRequest.text)
    for line in contents:
        data = line["clone_url"]
        os.system('git clone ' + data)

multiCloneGitHubUserRepos('TechnoCannon1337')
