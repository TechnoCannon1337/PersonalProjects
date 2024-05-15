import os
import os.path
import requests
import json
import time

def deleteAllGitHubRepos(gitHubTargetUser, myToken, pageCount='1000'):
    baseURL = 'https://api.github.com/users/'
    pageQuery ='/repos?per_page='
    gitHubRequest=requests.get(baseURL + gitHubTargetUser + pageQuery + pageCount)
    contents = json.loads(gitHubRequest.text)
    formatHead = {'Accept': 'application/vnd.github+json',
                'X-GitHub-Api-Version': '2022-11-28',
                'Authorization': 'Bearer {}'.format(myToken)}
    for line in contents:
        data = line["url"]
        cleanData = data.strip()
        deleteResponse = requests.delete(cleanData, headers = formatHead)
        if deleteResponse.status_code != 204:
            print(deleteResponse.content)
        else:
            print(cleanData + ' has been deleted.')
        time.sleep(1)

deleteAllGitHubRepos('YourGitHubUserName', 'YourPersonalAccessToken')
