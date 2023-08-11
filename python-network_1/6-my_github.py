#!/usr/bin/python3
"""
This script uses the GitHub API to display the user id.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-my_github.py <username> <access_token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, access_token))

    try:
        json_data = response.json()
        if "id" in json_data:
            print(json_data["id"])
        else:
            print("None")
    except ValueError:
        print("None")
