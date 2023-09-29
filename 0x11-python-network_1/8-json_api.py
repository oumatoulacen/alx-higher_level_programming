#!/usr/bin/python3
'''
Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
'''


import sys
import requests

if __name__ == "__main__":
    q = ""
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    data = {"q": q}
    req = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        jsn = req.json()
        if jsn:
            print(f"[{js.id}]: {js.name}")
        else:
            print("No result"
    except ValueError:
        print("Not a valid JSON")
