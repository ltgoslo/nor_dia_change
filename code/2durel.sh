#!/bin/sh

for i in ${1}${2}*.json.gz
do
    echo ${i}
    python3 code/json2durel.py ${i} ${2}
done