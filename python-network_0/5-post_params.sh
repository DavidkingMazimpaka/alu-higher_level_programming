#!/bin/bash
# Send a POST request URL and display the body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
