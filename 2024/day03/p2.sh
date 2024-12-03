cat $1 | grep -Po "(do\(\)|don\'t\(\))|(mul\(\d+\,\d+\))" | tr -d "mul'()" | awk -F ',' '
BEGIN {d = "true"; s = 0}
{
    if ($0 == "do") {
        d = "true";
    } else if ($0 == "dont") {
        d = "false";
    } else {
        s += (d == "true") ? ($1*$2) : 0;
    }
}
END {print s}
'