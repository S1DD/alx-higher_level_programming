#!/usr/bin/python3
"""

"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"a": letter}
    
    r = requests.post("http://0.0.0.0:5000/search_user", data=values)

    try:
        res = r.json()
        if res == {}:
            print("No result")

        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a vaid JSON")
