#!/usr/bin/expect
if [ $# -ne 1 ]; then
    echo "Usage: $0 cmd"
    exit 1
fi

cmd=$1
for n in 141 142 143 144
do
    echo "$n==============================================="
    # expect 1808.exp 192.168.5.$n "$cmd"
    ssh root@192.168.5.$n "$cmd"
done
