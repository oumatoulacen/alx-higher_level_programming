#!/usr/bin/python3
'''
Write a Python script that takes your GitHub credentials
'''


import requests
import sys

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    try:
        req = requests.get(url)
        commits = req.json()
        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}:", author_name)
    except Exception as e:
        print("Error:", e)
