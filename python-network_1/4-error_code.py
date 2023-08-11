#!/usr/bin/python3
"""
This script sends a request to a URL and displays the response body.
If the HTTP status code is >= 400, an error message is displayed.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command line arguments

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
