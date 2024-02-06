#!/bin/bash
#
# serve some local content (which has been created with "tox -e docs"), this
# convenience script autodetects a free port starting from 5000, and prints
# out the URL to this local site.
#
port=5000
while sudo lsof -i4:$port -sTCP:LISTEN -t; do
    port=$((port + 1))
done

cd doc/build/html

# autodetect EIP via meta data service:
ip=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)

echo "Open web browser at http://$ip:$port/"
python -m http.server $port
