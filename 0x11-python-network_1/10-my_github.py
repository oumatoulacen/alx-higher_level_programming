#!/usr/bin/python3
'''
Write a Python script that takes your GitHub credentials
'''


import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"

    try:
        req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
        json = req.json()
        print(json.get("id"))
    except Exception as e:
        print("Error:", e)
