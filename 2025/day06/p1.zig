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

    var rows: std.ArrayList(std.ArrayList(u64)) = .empty;
    defer {
        for (rows.items) |*sublist| sublist.deinit(allocator);
        rows.deinit(allocator);
    }
    var ops: std.ArrayList(u8) = .empty;
    defer ops.deinit(allocator);

    while (lines.next()) |line| {
        if (line.len == 0) continue;
        var sublist: std.ArrayList(u64) = .empty;

        var number_it = std.mem.splitScalar(u8, line, ' ');
        while (number_it.next()) |number| {
            // print("number:<{s}>\n", .{number});
            if (number.len == 0) continue;
            // print("not 0 \n", .{});
            if (number[0] < 48) {
                // print("not num \n", .{});
                try ops.append(allocator, number[0]);
            } else {
                // print("op \n", .{});
                try sublist.append(allocator, try util.parseIntDec(u64, number));
            }
        }

        if (sublist.items.len != 0) {
            try rows.append(allocator, sublist);
        } else sublist.deinit(allocator);
    }

    // print("{any}\n", .{rows.items});

    // print("{s}\n", .{ops.items});

    var grand_total: u64 = 0;

    for (ops.items, 0..) |op, col| {
        var temp_accumulator: u64 = 0;
        for (rows.items) |row| {
            switch (op) {
                '+' => temp_accumulator += row.items[col],
                '*' => {
                    if (temp_accumulator == 0) {
                        temp_accumulator = row.items[col];
                    } else temp_accumulator *= row.items[col];
                },
                else => unreachable,
            }
        }

        // print("accum{}\n", .{temp_accumulator});

        grand_total += temp_accumulator;
    }

    print("{}\n", .{grand_total});
}
