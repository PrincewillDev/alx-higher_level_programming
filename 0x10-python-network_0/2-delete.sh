#!/bin/bash
# Sends a DELETE request to URL passed to it and displays response body
curl -s -X DELETE "${1}"
