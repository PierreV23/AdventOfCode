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

pub fn readUntilEOF(allocator: std.mem.Allocator) ![]const u8 {
    const stdin = std.fs.File.stdin();

    const contents = try stdin.readToEndAlloc(allocator, std.math.maxInt(usize));
    return contents;
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

pub fn getCoords8(row: anytype, col: @TypeOf(row)) [8][2]@TypeOf(row) {
    // zig fmt: off
    const deltas = [8][2]@TypeOf(row){
        .{-1, -1}, .{-1, 0}, .{-1, 1},
        .{0, -1},            .{0, 1},
        .{1, -1},  .{1, 0},  .{1, 1},
    };

    var coords: [8][2]@TypeOf(row) = undefined;
    inline for (deltas, 0..) |delta, i| {
        coords[i] = .{ row + delta[0], col + delta[1] };
    }
    return coords;
}

pub fn getCoords4(row: anytype, col: @TypeOf(row)) [4][2]@TypeOf(row) {
    // zig fmt: off
    const deltas = [8][2]@TypeOf(row){
                   .{-1, 0},
        .{0, -1},            .{0, 1},
                   .{1, 0},
    };

    var coords: [8][2]@TypeOf(row) = undefined;
    inline for (deltas, 0..) |delta, i| {
        coords[i] = .{ row + delta[0], col + delta[1] };
    }
    return coords;
}


pub fn isWithinGrid(height: anytype, width: @TypeOf(height), row: @TypeOf(height), col: @TypeOf(height)) bool {
    return (0 <= row and row < height) and (0 <= col and col < width);
}


pub fn parseIntDec(comptime T: type, buf: []const u8) !T {
    return try std.fmt.parseInt(T, buf, 10);
}

pub fn withinIncl(left: anytype, right: @TypeOf(left), number: @TypeOf(left)) bool {
    return left <= number and number <= right;
}

pub fn overlapIncl(
    range1_left: anytype,
    range1_right: @TypeOf(range1_left),
    range2_left: @TypeOf(range1_left),
    range2_right: @TypeOf(range1_left),
) ?[2]@TypeOf(range1_left) {
    if (withinIncl(range1_left, range1_right, range2_left) or withinIncl(range1_left, range1_right, range2_right)) {
        return .{@min(range1_left, range2_left), @max(range1_right, range2_right)};
    }

    return null;
}



pub fn split(allocator: std.mem.Allocator, slice: anytype, delimiter: []const @typeInfo(@TypeOf(slice)).pointer.child) !std.ArrayList(@TypeOf(slice)) {
    const element_type = @typeInfo(@TypeOf(slice)).pointer.child;

    var seq: std.ArrayList(@TypeOf(slice)) = .empty;
    errdefer seq.deinit(allocator);

    if (delimiter.len == 1) {
        var it = std.mem.splitScalar(element_type, slice, delimiter[0]);
        while (it.next()) |el| {
            try seq.append(allocator, el);
        }
    } else {
        var it = std.mem.splitSequence(element_type, slice, delimiter);
        while (it.next()) |el| {
            try seq.append(allocator, el);
        }
    }

    return seq;
}

pub fn Point(comptime T: type) type {
    return struct {
        row: T,
        col: T
    };
}
