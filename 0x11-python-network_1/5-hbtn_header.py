#!/usr/bin/python3
"""
Sends a request to a given URL, and displays the value of X-Request-Id response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
    
