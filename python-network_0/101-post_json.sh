#!/bin/bash
# Json POST must be sent to URL
curl -sX POST -H "Content-type: application/json" -H "Accept: application/json" -d "@$2" "$1"
