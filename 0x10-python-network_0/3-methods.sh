#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sIX OPTIONS "$1" | grep -i "Allow:" | cut -d " " -f 2-
