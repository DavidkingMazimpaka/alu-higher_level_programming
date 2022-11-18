#!/bin/bash
# send request to URL and determine the size of the body
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
