#!/bin/bash
# Tcript sends a POST request to a URL received and displays response body
curl -sd "email=test@gmail.com&&subject=I will always be here for PLD" -X POST "$1"
