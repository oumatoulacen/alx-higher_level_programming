#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email address, sends
a POST request to the passed URL with the email as a parameter, and
finally displays the body of the response.
'''


import sys
import requests

url = sys.argv[1]
email = sys.argv[2]
data = {"email": email}

try:
    response = requests.post(url, data=data)
    print(response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
