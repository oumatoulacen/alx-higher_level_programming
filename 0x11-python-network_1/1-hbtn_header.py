#!/usr/bin/python3
'''Write a Python script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable found in
the header of the response.
'''


import urllib.request
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        request_id = response.headers['X-Request-Id']
        print(request_id)
except urllib.error.URLError as e:
    print("Error:", e)
