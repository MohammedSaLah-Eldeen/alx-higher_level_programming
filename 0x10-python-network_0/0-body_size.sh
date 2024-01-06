#!/bin/bash
# task 0

curl --head -s $1 | awk '/Content-Length/ {print $2}'
