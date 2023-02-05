#! /bin/bash
chmod +x ./controller.sh
chmod +x ./server/server.sh
# Run the server
./server/server.sh &
sleep 2
# Run the controller to check if the server runs and fool it 
# with France database
./controller.sh &
wait