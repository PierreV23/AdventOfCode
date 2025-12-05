const util = @import("util");
const std = @import("std");

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();

    const allocator = gpa.allocator();

    var w = std.fs.File.stdout().writer(&.{});
    const stdout = &w.interface;

    const text = try util.readUntilBlank(allocator);
    defer allocator.free(text);

    var lines = std.mem.splitScalar(u8, text, '\n');
    const line = lines.next().?;

    var ranges = std.mem.splitScalar(u8, line, ',');

    while (ranges.next()) |range| {
        var numbers = std.mem.splitScalar(u8, range, '-');

        const n1 = try std.fmt.parseInt(u64, numbers.next().?, 10);
        const n2 = try std.fmt.parseInt(u64, numbers.next().?, 10);

        for (n1..n2 + 1) |number| {
            try stdout.print("{}\n", .{number});
        }
    }
}
