#!/bin/bash
# Send a request to URL and pass an argument
curl -o /dev/null -sw "%{http_code}" "$1"
