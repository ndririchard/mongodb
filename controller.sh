#! /bin/bash
ps -aux | grep mongod
# Import the France database
mongoimport -d=France -c=communes --type csv data/communes-departement-region.csv --headerline --port 6024