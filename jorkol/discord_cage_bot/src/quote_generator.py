import json

import requests


def random_quote():
    result = requests.get("https://api.quotable.io/random")
    return json.loads(result.text)["content"]


if __name__ == "__main__":
    print(random_quote())
