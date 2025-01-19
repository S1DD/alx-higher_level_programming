#!/usr/bin/python3
"""Sends a POST request to URL, with a given email
 Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email", sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
    
