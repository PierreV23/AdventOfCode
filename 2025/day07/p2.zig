const util = @import("util");
const std = @import("std");

const print = @import("std").debug.print;

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();

    const allocator = gpa.allocator();

    const text = try util.readUntilEOF(allocator);
    defer allocator.free(text);

    var lines_list = try util.split(allocator, text, "\n"[0..]);
    if (lines_list.items[lines_list.items.len - 1].len == 0) _ = lines_list.pop().?;
    const lines = try lines_list.toOwnedSlice(allocator);
    defer allocator.free(lines);

    // print("{any}\n", .{lines});

    var prev = std.AutoHashMap(u64, u64).init(allocator);
    defer prev.deinit();

    const start_col = std.mem.indexOfScalar(u8, lines[0], 'S').?;

    try prev.put(start_col, 1);

    var count: usize = 0;
    count = 0;

    for (lines) |line| {
        var curr = std.AutoHashMap(u64, u64).init(allocator);
        // defer curr.deinit();
        var queue = prev.iterator();

        while (queue.next()) |q| {
            const col = q.key_ptr.*;
            const val = q.value_ptr.*;

            var cols: [2]?u64 = .{ null, null };
            if (line[col] == '^') {
                cols[0] = col - 1;
                cols[1] = col + 1;
            } else {
                cols[0] = col;
            }

            for (cols) |some_col| {
                if (some_col) |new_col| {
                    var new_val = val;
                    if (curr.get(new_col)) |existing_val| new_val += existing_val;

                    try curr.put(new_col, new_val);
                }
            }
        }

        prev.deinit();
        prev = curr;
    }

    var queue = prev.iterator();
    while (queue.next()) |q| {
        count += q.value_ptr.*;
    }

    print("{}\n", .{count});
}
