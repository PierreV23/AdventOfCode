cat $1 | egrep -v '\||^$' | awk "$(cat $1 | grep '|' | perl -pe 's|(\d+).(\d+)|!/$2.+$1/|g' | tr -d '\n' | sed 's/\/!/\/ \&\& !/g')" | awk -F ',' '{s += $(NF/2+1)} END {print s}'
