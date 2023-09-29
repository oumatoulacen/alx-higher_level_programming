#!/usr/bin/python3
'''
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
'''


import urllib
import sys

if __name__ == "__main__":
    try:
        with urllib.request.Request(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
