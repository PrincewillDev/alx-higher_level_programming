#!/bin/bash
# This script takes in URL, sends GET request
# to it and displays response body
curl -s -H "X-School-User-Id: 98" "$1"