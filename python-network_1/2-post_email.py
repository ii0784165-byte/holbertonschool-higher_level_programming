#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("utf-8")

    req = request.Request(url, data=data, method="POST")

    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
