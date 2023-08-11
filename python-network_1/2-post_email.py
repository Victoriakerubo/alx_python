#!/usr/bin/python3
"""
This script sends a POST request with an email parameter and displays the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command line arguments
    email = sys.argv[2]  # Get the email from command line arguments

    payload = {"email": email}
    response = requests.post(url, data=payload)

    print(response.text)
