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

    while (lines.next()) |line| {
        if (line.len == 0) continue;
    }
}
