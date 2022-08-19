#!/bin/sh

cd doc/build/html
python3 -m http.server 5000
