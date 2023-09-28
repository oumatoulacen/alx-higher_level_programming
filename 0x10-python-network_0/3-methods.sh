#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS $1 | awk '/^Allow:/ {print $2}'
