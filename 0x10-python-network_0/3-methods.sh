#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -I -s -X OPTIONS $1 2>&1 | grep Allow | awk -F': ' '{print $2}'
