#!/bin/bash
# Send the request using curl and display only the status code
curl -s -o /dev/null -w "%{http_code}\n" "$URL"
