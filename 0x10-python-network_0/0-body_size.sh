#!/usr/bin/env bash
# Bash script that displays the size of the body of the response
curl -s --head "$1" | grep 'Content-Length' | cut -d ' ' -f 2
