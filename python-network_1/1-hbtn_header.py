#!/usr/bin/python3
"""
This script fetches the value of the X-Request-Id header from a URL response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command line arguments
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
