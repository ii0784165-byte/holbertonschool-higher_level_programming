#!/usr/bin/python3
"""Script that sends a letter to a server and handles JSON response"""

import requests
import sys

# Get the letter argument or default to empty string
q = sys.argv[1] if len(sys.argv) > 1 else ""

url = "http://0.0.0.0:5000/search_user"
data = {'q': q}

try:
    response = requests.post(url, data=data)
    response_json = response.json()
    if response_json:
        print(f"[{response_json.get('id')}] {response_json.get('name')}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
except requests.RequestException as e:
    print(f"Error: {e}")
