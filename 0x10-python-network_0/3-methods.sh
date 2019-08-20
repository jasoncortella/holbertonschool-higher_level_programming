#!/bin/bash
# takes in URL, displays all HTTP methods the server will accept
curl -sI $1 | grep "Allow: " | cut -d " " -f2-
