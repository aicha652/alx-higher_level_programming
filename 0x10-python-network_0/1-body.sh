#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/null -w "Route %{http_code}" $1
