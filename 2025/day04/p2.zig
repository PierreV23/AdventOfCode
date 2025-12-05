const util = @import("util");
const std = @import("std");

const print = @import("std").debug.print;

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();

    const allocator = gpa.allocator();

    const text = try util.readUntilBlank(allocator);
    defer allocator.free(text);

    var lines_it = std.mem.splitScalar(u8, text, '\n');

    var lines_list: std.ArrayList([]u8) = .empty;

    while (lines_it.next()) |line| {
        if (line.len == 0) continue;

        const mutable_line = try allocator.dupe(u8, line);
        try lines_list.append(allocator, mutable_line);
    }

    var lines = try lines_list.toOwnedSlice(allocator);
    defer {
        for (lines) |line| {
            allocator.free(line);
        }
        allocator.free(lines);
    }

    const HEIGHT: isize = @intCast(lines.len);
    const WIDTH: isize = @intCast(lines[0].len);

    var count: u64 = 67; // L
    var total_removed: u64 = 0;
    while (count > 0) {
        count = 0;

        for (lines, 0..) |row, row_idx| {
            // print("\n", .{});
            for (row, 0..) |cell, col_idx| {
                if (cell != '@') continue;

                // print("{c}", .{cell});
                var tp_count: u64 = 0;

                const surrounding = util.getCoords8(@as(isize, @intCast(row_idx)), @as(isize, @intCast(col_idx)));

                for (surrounding) |coord| {
                    const row_idx_other, const col_idx_other = coord;
                    if (!util.isWithinGrid(HEIGHT, WIDTH, row_idx_other, col_idx_other)) continue;

                    if (lines[@intCast(row_idx_other)][@intCast(col_idx_other)] == '@') tp_count += 1;
                }

                if (tp_count < 4) {
                    count += 1;
                    lines[row_idx][col_idx] = '.';
                }
            }
        }

        total_removed += count;
    }

    print("{}\n", .{total_removed});
}
