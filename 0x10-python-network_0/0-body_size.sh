#!/bin/bash
# task 0: getting the size of the of body (content) in the response.
curl -s --head "$1" | awk '/Content-Length/ {print $2}'
