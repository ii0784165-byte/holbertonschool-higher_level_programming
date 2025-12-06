#!/usr/bin/python3
"""
Send a request to a URL and display the body.
If the HTTP status code >= 400, print an error code instead.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.RequestException as e:
        print(f"Error: {e}")
