const std = @import("std");
const aoclib = @import("aoclib");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var buf: [std.os.PATH_MAX]u8 = undefined;
    const cwd = try std.os.getcwd(&buf);

    var args = try std.process.argsWithAllocator(allocator);
    defer args.deinit();
    // _ = args.skip();
    try stdout.print("cwd={s}\n", .{cwd});
    while (args.next()) |arg| {
        std.debug.print(" {s}\n", .{arg});
    }

    try stdout.print("{c}", .{aoclib.testt()});
}
