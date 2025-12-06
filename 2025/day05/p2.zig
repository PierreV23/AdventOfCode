const util = @import("util");
const std = @import("std");

const print = @import("std").debug.print;

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();

    const allocator = gpa.allocator();

    const text = try util.readUntilEOF(allocator);
    defer allocator.free(text);

    var chunks = std.mem.splitSequence(u8, text, "\n\n");
    var ranges = std.mem.splitScalar(u8, chunks.next().?, '\n');
    // var IDs = std.mem.splitScalar(u8, chunks.next().?, '\n');

    var ranges_list: std.ArrayList([2]usize) = .empty;
    defer ranges_list.deinit(allocator);

    var max_end: usize = 0;

    while (ranges.next()) |range_line| {
        if (range_line.len == 0) continue;
        var ranges_split = std.mem.splitScalar(u8, range_line, '-');
        const start = try util.parseIntDec(usize, ranges_split.next().?);
        const end = try util.parseIntDec(usize, ranges_split.next().?);
        try ranges_list.append(allocator, .{ start, end });
        // print("{} {}\n", .{ max_end, end });
        max_end = @max(max_end, end);
    }

    var overlap_found = true;

    outer: while (overlap_found) {
        for (ranges_list.items, 0..) |range1, range1_idx| {
            for (ranges_list.items, 0..) |range2, range2_idx| {
                if (range1_idx == range2_idx) continue;
                // print("{any} {any} {any} {any} {any} \n", .{ ranges_list.items, range1, range1_idx, range2, range2_idx });
                if (util.overlapIncl(range1[0], range1[1], range2[0], range2[1])) |new| {
                    _ = ranges_list.swapRemove(@max(range1_idx, range2_idx));
                    _ = ranges_list.swapRemove(@min(range1_idx, range2_idx));
                    try ranges_list.append(allocator, new);
                    continue :outer;
                }
            }
        }

        overlap_found = false;
    }

    var fresh_count: usize = 0;
    for (ranges_list.items) |range| fresh_count += range[1] - (range[0] - 1);
    print("{}\n", .{fresh_count});
}
