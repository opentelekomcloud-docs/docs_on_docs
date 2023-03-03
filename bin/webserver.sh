#!/bin/bash

port=5000

while sudo lsof -i4:$port -sTCP:LISTEN -t; do
    port=$((port + 1))
done

cd doc/build/html

ip=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)

echo "Open web browser at http://$ip:$port/"
python -m http.server $port
