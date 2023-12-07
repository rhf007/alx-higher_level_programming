#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response, it does seem that -L doesnt get along with other options
curl -sL $1
