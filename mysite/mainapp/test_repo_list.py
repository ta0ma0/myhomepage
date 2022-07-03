import requests
import json

USER='ta0ma0'
API_TOKEN='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'
GIT_API_URL=f'https://api.github.com/users/{USER}/repos'

header = {"Accept": "application/vnd.github+json",
        "Authorization": API_TOKEN}

def get_repos(url):
    query = requests.get(url, headers=header)
    jsonAnswer = query.json()
    # print(jsonAnswer)
    return jsonAnswer

count = 0
for el in get_repos(GIT_API_URL):
    print(el)
    count += 1
print("Всего проектов", count)