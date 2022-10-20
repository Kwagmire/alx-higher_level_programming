#!/bin/bash
# Get response from a given URL to a GET request that included a header variable
curl -H "X-School-User-Id: 98" "$1"
