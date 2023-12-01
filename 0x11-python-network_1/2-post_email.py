#!/usr/bin/python3
"""Python script that takes in a URL and an email,sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    with urllib.request.urlopen(url, mail) as response:
        email = response.read().decode()
        print(email)
