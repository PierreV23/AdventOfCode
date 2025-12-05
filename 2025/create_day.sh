#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <day_folder>"
    echo "Example: $0 day01"
    exit 1
fi

INPUT=$1

if ! [[ $INPUT =~ ^day[0-2][0-9]$ ]]; then
    echo "Invalid pattern"
    exit 1
fi

if [ -d "$INPUT" ]; then
    echo "Folder '$INPUT' already exists"
    exit 1
fi

mkdir "$INPUT"
echo "Created folder: $INPUT"

read -r -d '' TEMPLATE << 'EOF'
const util = @import("util");
const std = @import("std");

const print = @import("std").debug.print;

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();

    const allocator = gpa.allocator();

    const text = try util.readUntilBlank(allocator);
    defer allocator.free(text);

    var lines = std.mem.splitScalar(u8, text, '\n');

    while (lines.next()) |line| {
        if (line.len == 0) continue;
    }
}
EOF


echo "$TEMPLATE" > "$INPUT/p1.zig"
echo "Created file: $INPUT/p1.zig"

echo "$TEMPLATE" > "$INPUT/p2.zig"
echo "Created file: $INPUT/p2.zig"
