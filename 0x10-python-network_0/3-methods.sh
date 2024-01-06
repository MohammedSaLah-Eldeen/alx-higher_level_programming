#!/bin/bash
# task 3: figuring allowed methods
curl -s --head "$1" | awk -F ': ' '/Allow/ {print $2}'
