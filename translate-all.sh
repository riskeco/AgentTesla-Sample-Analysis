#!/bin/sh

rm -rf unconfused-readble-sources

cp -a unconfused-sources unconfused-readble-sources

find unconfused-readble-sources/ -name '*cs' -exec python3 ./translate.py {} \;
