const std = @import("std");

pub fn readUntilBlank(allocator: std.mem.Allocator) ![]const u8 {
    const stdin = std.fs.File.stdin();
    var buf: [4096]u8 = undefined;
    var reader = stdin.reader(&buf);
    const r = &reader.interface;

    var result: std.ArrayList(u8) = .empty;
    errdefer result.deinit(allocator);

    var line_buf = std.Io.Writer.Allocating.init(allocator);
    defer line_buf.deinit();

    while (true) {
        _ = r.streamDelimiter(&line_buf.writer, '\n') catch |err| {
            if (err == error.EndOfStream) break;
            return err;
        };
        _ = r.toss(1);

        if (line_buf.written().len == 0) break;

        try result.appendSlice(allocator, line_buf.written());
        try result.append(allocator, '\n');
        line_buf.clearRetainingCapacity();
    }

    return result.toOwnedSlice(allocator);
}

pub fn intIsEven(n: anytype) bool {
    return (n & 0b1) == 0;
}

pub fn maxIdx(slice: anytype) ?usize {
    const inner_type = @typeInfo(@TypeOf(slice)).pointer.child;
    var high: ?inner_type = null;
    var high_idx: ?usize = null;

    for (slice, 0..) |el, idx| {
        if (high) |some| {
            if (some < el) {
                high = el;
                high_idx = idx;
            }
        } else {
            high = el;
            high_idx = idx;
        }
    }

    return high_idx;
}

pub fn max(slice: anytype) ?@typeInfo(@TypeOf(slice)).pointer.child {
    const inner_type = @typeInfo(@TypeOf(slice)).pointer.child;
    var high: ?inner_type = null;

    for (slice) |el| {
        if (high) |some| {
            if (some < el) {
                high = el;
            }
        } else {
            high = el;
        }
    }

    return high;
}
