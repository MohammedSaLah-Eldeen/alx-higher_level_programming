#!/bin/bash
# task: sending data with a POST request
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
