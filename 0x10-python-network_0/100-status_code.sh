#!/bin/bash
# Send the request using curl and display only the status code
curl -so /dev/null -w %{http_code} $1
