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

    var lines_list: std.ArrayList([]const u8) = .empty;
    defer lines_list.deinit(allocator);

    while (lines.next()) |line| {
        if (line.len == 0) continue;
        try lines_list.append(allocator, line);
    }

    var columns: std.ArrayList([]u64) = .empty;
    defer {
        for (columns.items) |sublist| allocator.free(sublist);
        columns.deinit(allocator);
    }

    var ops: std.ArrayList(u8) = .empty;
    defer ops.deinit(allocator);

    var col_idx: usize = 0;
    var had_char = true;
    var had_digit = false;

    var column: std.ArrayList(u64) = .empty;
    defer column.deinit(allocator);

    while (had_char) {
        var number: std.ArrayList(u8) = .empty;
        defer number.deinit(allocator);
        had_digit = false;
        had_char = false;
        line_loop: for (lines_list.items) |line| {
            if (col_idx >= line.len) continue else had_char = true;
            const char = line[col_idx];
            switch (char) {
                '0'...'9' => {
                    try number.append(allocator, char);
                    had_digit = true;
                },
                '+', '*' => {
                    try ops.append(allocator, char);
                    break :line_loop;
                },
                ' ' => continue,
                else => unreachable,
            }
        }

        if (had_digit) {
            const slice = try number.toOwnedSlice(allocator);
            defer allocator.free(slice);
            const num = try util.parseIntDec(u64, slice);
            try column.append(allocator, num);
        } else {
            try columns.append(allocator, try column.toOwnedSlice(allocator));
        }

        col_idx += 1;
    }

    // print("{any}\n", .{columns.items});
    // print("{any}\n", .{ops.items});

    var grand_total: u64 = 0;

    for (columns.items, ops.items) |col, op| {
        var temp_accumulator: u64 = 0;
        for (col) |num| {
            switch (op) {
                '+' => temp_accumulator += num,
                '*' => {
                    if (temp_accumulator == 0) {
                        temp_accumulator = num;
                    } else temp_accumulator *= num;
                },
                else => unreachable,
            }
        }

        grand_total += temp_accumulator;
    }

    print("{}\n", .{grand_total});
}
