cat input.txt | xargs -I {} sh -c $'echo "$1" | cut -d" " -f1 | fold -1 | sort | uniq -c | sort -r | awk \'{print $1}\' | tr "\n" "\t" | awk \'BEGIN {FS="\t"} {print $1, ($2==""?"0":$2)}\' | tr "\n" " "  && echo "$1" | cut -d" " -f1 | fold -1 | awk \'{print index("23456789TJQKA", $1)}\' | tr "\n" " " && echo "$1" | awk \'{print $1, $2}\'' _ {} | tr " " "\t" | sort -k1n -k2n -k3n -k4n -k5n -k6n -k7n | awk 'BEGIN {c=0} {c+=1;s+=$9*c;print c, s, $8, $9} END {print s}' | tr " " "\t"