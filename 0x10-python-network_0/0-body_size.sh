#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL
# and displays the size of the body of the response

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL passed as an argument
URL="$1"

# Send a curl request to the URL and save the response body to a temporary file

curl -s "$URL" | wc -c 
