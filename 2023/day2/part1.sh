cat input.txt | egrep -v '(([1-9][3-9]|[2-9]0) red|([1-9][4-9]|[2-9]0) green|([1-9][5-9]|[2-9]0) blue)' | cut -d':' -f1 | cut -d' ' -f2 | awk '{s+=$1} END {print s}'

cat input.txt | egrep -v '[1-9]([3-9] red|[4-9] green|[5-9] blue)' | cut -d':' -f1 | cut -d' ' -f2 | awk '{s+=$1} END {print s}'