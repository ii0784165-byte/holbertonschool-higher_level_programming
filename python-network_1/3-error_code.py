#!/usr/bin/python3
"""Fetches URL and handles HTTP errors"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
