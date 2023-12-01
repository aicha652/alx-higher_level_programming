#!/usr/bin/python3
import urllib.request
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", html.__class__)
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode("utf-8"))
