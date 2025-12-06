#!/usr/bin/python3
"""Python script that uses GitHub API and Basic Auth to get user id"""

import sys
import requests

username = sys.argv[1]
password = sys.argv[2]  # Personal access token

url = "https://api.github.com/user"

try:
    response = requests.get(url, auth=(username, password))
    response_json = response.json()
    print(response_json.get("id"))
except requests.RequestException:
    print(None)
