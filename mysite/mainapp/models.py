from itertools import count
from django.db import models
import requests
import json
from mainapp.settings import API_TOKEN

# Create your models here.

def count_git_projects(GIT_API_URL):
    counter = 0
    header = {"Accept": "application/vnd.github+json",
            "Authorization": API_TOKEN}
    try:
        query = requests.get(GIT_API_URL, headers=header)
        jsonAnswer = query.json()
        for el in jsonAnswer:
            counter += 1
            count_progects = counter
    except Exception as er:
        return "Fail get api " + str(er)
        # print(jsonAnswer)

    return count_progects