#!/bin/bash
# sends a JSON POST request with a given JSON file to a given URL
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
