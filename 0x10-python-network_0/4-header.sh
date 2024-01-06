#!/bin/bash
# task 4: adding a request header
curl -s "$1" -H "X-School-User-Id: 98"
