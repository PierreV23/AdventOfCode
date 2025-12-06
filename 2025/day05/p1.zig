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
    var IDs = std.mem.splitScalar(u8, chunks.next().?, '\n');

    var ranges_list: std.ArrayList([2]usize) = .empty;
    defer ranges_list.deinit(allocator);

    while (ranges.next()) |range_line| {
        if (range_line.len == 0) continue;
        var ranges_split = std.mem.splitScalar(u8, range_line, '-');
        try ranges_list.append(allocator, .{ try util.parseIntDec(usize, ranges_split.next().?), try util.parseIntDec(usize, ranges_split.next().?) });
    }

    var fresh_count: u64 = 0;

    while (IDs.next()) |id_string| {
        if (id_string.len == 0) continue;
        // print("something:<{}>\n", .{id_string});
        const id = try util.parseIntDec(usize, id_string);
        for (ranges_list.items) |range| {
            if (util.within(range[0], range[1], id)) {
                fresh_count += 1;
                break;
            }
        }
    }

    print("{}\n", .{fresh_count});
}
