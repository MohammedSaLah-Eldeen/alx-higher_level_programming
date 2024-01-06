#!/bin/bash
# getting back the status code.
curl -s --head -o /dev/null -w "%{http_code}" "$1"
