#!/usr/bin/python3
"""script that sends a request to the URL and displays the body of the
response. If an error occurs, the script will manage the error and display"""

import requests
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <URL>")
        sys.exit(1)

    reply = requests.get(sys.argv[1])
    if reply.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
