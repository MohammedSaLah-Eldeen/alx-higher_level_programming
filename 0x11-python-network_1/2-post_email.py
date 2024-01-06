#!/usr/bin/python3
"""
task 2
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {
        'email': email,
    }
    data = urllib.parse.urlencode(params).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
