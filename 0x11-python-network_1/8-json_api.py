#!/usr/bin/python3
'''
Write a Python script that takes in a letter and sends a POSTvrequest
to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''


import sys
import requests

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        jsn = req.json()
        if jsn:
            print(f"[{jsn.get('id')}]: {jsn.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
