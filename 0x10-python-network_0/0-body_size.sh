#!/bin/bash
# task 0: getting the size of the of body (content) in the response.

curl -s $1 | wc -c 
