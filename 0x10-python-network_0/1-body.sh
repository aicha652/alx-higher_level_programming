#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
sh -c "[$(curl -o -I -L -s -w 'Route %{http_code}' $1) -eq 200]"
