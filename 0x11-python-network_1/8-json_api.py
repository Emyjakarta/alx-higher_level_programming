#!/usr/bin/python3
"""script that sends a POST request to a URL with a letter as a parameter"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        i = sys.argv[1]
    else:
        i = ""

    url = "http://0.0.0.0:5000/search_user"

    reply = requests.post(url, data={"i": i})
    try:
        json_reply = reply.json()
        if json_reply:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
