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

    const Point = util.Point(usize);

    var map = std.AutoHashMap(Point, bool).init(allocator);
    defer map.deinit();

    const start: Point = .{
        .row = 0,
        .col = std.mem.indexOfScalar(u8, lines[0], 'S').?,
    };

    const HEIGHT = lines.len;
    const WIDTH = lines[0].len;

    var queue: std.ArrayList(Point) = .empty;
    defer queue.deinit(allocator);

    try queue.append(allocator, start);

    var count: usize = 0;

    var i: usize = 0;
    while (i < queue.items.len) : (i += 1) {
        const point = queue.items[i];
        // print("{any}\n", .{point});
        const row = point.row;
        const col = point.col;
        if ((!util.isWithinGrid(HEIGHT, WIDTH, row, col)) or
            map.contains(point)) continue;
        try map.put(point, true);
        if (lines[row][col] == '^') {
            count += 1;
            try queue.append(allocator, .{ .row = row, .col = col - 1 });
            try queue.append(allocator, .{ .row = row, .col = col + 1 });
        } else {
            try queue.append(allocator, .{ .row = row + 1, .col = col });
        }
    }

    print("{}\n", .{count});
}
