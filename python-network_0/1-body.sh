#!/bin/bash
# Sends a GET request (following redirects) and displays the body only if final status is 200
response=$(curl -s -L -w "\n%{http_code}" "$1")
status=$(echo "$response" | tail -1)
body=$(echo "$response" | sed '$d')

if [ "$status" -eq 200 ]; then
    echo "$body"
fi
