#!/usr/bin/python3
"""script that sends a request to the URL and displays the body of the
response. If an error occurs, the script will manage the error and display"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <URL>")
        sys.exit(1)

    url = sys.argv[1]
    requ = Request(url)

    try:
        with urlopen(requ) as reply:
            print(reply.read().decode('utf-8'))
    except HTTPError as err:
        print(f"Error code: {err.code}")
