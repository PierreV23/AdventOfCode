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

    var rot: isize = 50;
    var count: usize = 0;

    while (lines.next()) |line| {
        if (line.len == 0) continue;

        const direction = line[0];
        var distance = try std.fmt.parseInt(i32, line[1..], 10);
        if (direction == 'L') distance *= -1;

        rot += distance;
        rot = @mod(rot, 100);

        if (rot == 0) count += 1;

        print("{s} {}\n", .{ line, rot });
    }

    print("Count: {}\n", .{count});
}
