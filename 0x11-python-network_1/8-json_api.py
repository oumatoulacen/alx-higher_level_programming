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
    if sys.argv[1]:
        q = sys.argv[1]
    data = {"q": q}
    req = requests.post("http://0.0.0.0:5000/search_user", data=data)
    js = re.json()
    if js == "":
        print("No result")
    else if type(js) == dict:
        print(f"[{js.id}]: {js.name}")
    else:
        print("Not a valid JSON")
