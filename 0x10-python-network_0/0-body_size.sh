#!/bin/bash
# takes in a URL, sends a request to it and displays size of response body
curl -s "${1}" | wc -c