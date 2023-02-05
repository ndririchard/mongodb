#! /bin/bash
# Here my server will run on the localhost:6024
# Create a data folder for my server
mkdir server/data
# basic setup
port=6024
host="127.0.0.1"
# Running the server in background
mongod --dbpath server/data --port $port 