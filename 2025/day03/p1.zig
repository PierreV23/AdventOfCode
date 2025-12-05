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

    var count: u64 = 0;

    while (lines.next()) |line| {
        if (line.len == 0) continue;

        const max_idx = util.maxIdx(line).?;

        var n1: ?u8 = null;
        var n2: ?u8 = null;

        if (max_idx == line.len - 1) {
            const max_left = util.max(line[0 .. line.len - 1]).?;
            n1 = max_left - 48;
            n2 = line[max_idx] - 48;
        } else {
            n1 = line[max_idx] - 48;
            n2 = util.max(line[max_idx + 1 ..]).? - 48;
        }
        // print("{}{}\n", .{ n1, n2 });
        count += n1.? * 10 + n2.?;
    }

    print("{}\n", .{count});
}
