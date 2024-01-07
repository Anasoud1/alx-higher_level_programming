#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}
    req = requests.post(url, data=data)
    try:
        value_json = req.json()
        if not value_json:
            print("No result")
        else:
            my_id = value_json.get("id")
            my_name = value_json.get("name")
            print("[{}] {}".format(my_id, my_name))
    except ValueError:
        print("Not a valid JSON")
