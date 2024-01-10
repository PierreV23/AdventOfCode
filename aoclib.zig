pub fn testt() u8 {
    return 'x';
}

const std = @import("std");
const Allocator = std.mem.Allocator;
const ArrayList = std.ArrayList;
const Reader = std.fs.File.Reader;

pub fn read_and_split(allocator: Allocator, reader: Reader, delimiter: []const u8, ignore_chars: []const u8) ![][]const u8 {
    // const stdout = std.io.getStdOut().writer();
    var collection = ArrayList([]const u8).init(allocator);
    // defer {
    //     for (collection.items) |e| {
    //         allocator.free(e);
    //     }
    //     collection.deinit();
    // }
    var is_end = false;
    var stack = ArrayList(u8).init(allocator);
    defer stack.deinit();
    var delimiter_stack = ArrayList(u8).init(allocator);
    defer delimiter_stack.deinit();
    var delimiter_idx: usize = 0;
    while (!is_end) {
        const c = reader.readByte() catch |err| switch (err) {
            error.EndOfStream => {
                is_end = true;
                break;
            },
            else => |e| return e,
        };
        if (std.mem.containsAtLeast(u8, ignore_chars, 1, &[_]u8{c})) continue;
        if (c == delimiter[delimiter_idx]) {
            // try stdout.print("counting delimiter {}\n", .{delimiter_idx});
            try delimiter_stack.append(c);
            delimiter_idx += 1;
        } else if (delimiter_idx > 0) {
            // try stdout.print("delimiter cancelled {} {c}\n", .{ delimiter_stack.items.len, c });
            // try stack.appendSlice(try delimiter_stack.toOwnedSlice());
            for (delimiter_stack.items) |tc| try stack.append(tc);
            delimiter_stack.clearAndFree();
            delimiter_idx = 0;
            try stack.append(c);
        } else {
            // try stdout.print("append to stack\n", .{});
            try stack.append(c);
        }
        if (delimiter_idx == delimiter.len) {
            // try stdout.print("full on delim\n", .{});
            delimiter_stack.clearAndFree();
            try collection.append(try stack.toOwnedSlice());
            delimiter_idx = 0;
        }
    }
    if (delimiter_stack.items.len > 0) {
        // try stdout.print("dstack leftover\n", .{});
        try stack.appendSlice(try delimiter_stack.toOwnedSlice());
    }
    if (stack.items.len > 0) {
        // try stdout.print("stack leftover\n", .{});
        try collection.append(try stack.toOwnedSlice());
    }

    return try collection.toOwnedSlice();
}

pub fn run_part(comptime I: type, comptime part_func: fn (allocator: Allocator, input: I) anyerror!?isize, allocator: Allocator, test_cases: []I, test_answers: []const isize, input: I) !?isize {
    const stdout = std.io.getStdOut().writer();
    for (test_cases, test_answers, 0..) |inp, corr, i| {
        const ans = try part_func(allocator, inp);
        if (ans == null) {
            try stdout.print("idx={} returned null\n", .{i});
        } else {
            try stdout.print("idx={} corr={} out={}\n", .{ i, corr, ans.? });
        }
    }
    const ans = (try part_func(allocator, input));
    return ans;
}
