cat $1 | grep -Po "(do\(\)|don\'t\(\))|(mul\(\d+\,\d+\))" | tr -d "mul'()" | awk -F ',' '
BEGIN {d = "do"; s = 0}
{
    if ($0 == "do") {
        d = "do";
    } else if ($0 == "dont") {
        d = "dont";
    } else {
        s += (d == "do") ? ($1*$2) : 0;
    }
}
END {print s}
'