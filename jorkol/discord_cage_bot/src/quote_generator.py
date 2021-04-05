"""This is a module that loads a random quotes"""

import json

import requests


def random_quote():
    result = requests.get("https://goquotes-api.herokuapp.com/api/v1/random?count=1")
    return json.loads(result.text)["quotes"][0]["text"]


if __name__ == "__main__":
    print(random_quote())
