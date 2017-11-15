#!/bin/sh
if [ $# -ne 2 ]; then
    echo "Usage: $0 file dir"
    exit 1
fi

file=$1
dir=$2
for n in 141 142 143 144
do
    #expect 1809.exp $file 192.168.5.$n $dir
    scp -rp $file root@192.168.5.$n:$dir
done
