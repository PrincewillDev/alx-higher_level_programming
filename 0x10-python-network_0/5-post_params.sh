#!/usr/bin/env bash

# This script sends a POST request to a URL
# received and displays response body
curl -s -X POST -d "email=test%40gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"