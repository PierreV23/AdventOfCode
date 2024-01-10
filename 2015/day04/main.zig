const std = @import("std");
const Allocator = std.mem.Allocator;
const ArrayList = std.ArrayList;
const Reader = std.fs.File.Reader;
const aoclib = @import("aoclib");
const read_and_split = aoclib.read_and_split;
const run_part = aoclib.run_part;
const Md5 = std.crypto.hash.Md5;

fn part1(allocator: Allocator, input: []const u8) anyerror!?isize {
    const stdout = std.io.getStdOut().writer();
    var hasher = Md5.init(.{});
    _ = hasher;
    var count: usize = 0;
    _ = count;
    // while (true) {
    var buf: [Md5.digest_length]u8 = undefined;
    Md5.hash(input, &buf, .{});
    // }
    // const as_hex: [16]u8 = undefined;
    var as_hex = ArrayList(u8).init(allocator);
    defer as_hex.deinit();
    try std.fmt.fmtSliceHexLower(&buf).format("{}", .{}, as_hex.writer());
    try stdout.print("{s} => {any} {s} {}", .{ input, buf, as_hex.items, std.mem.startsWith(u8, as_hex.items, "e8") });
    return null;
}

fn part2(allocator: Allocator, input: []const u8) anyerror!?isize {
    _ = input;
    _ = allocator;
    return null;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    _ = stdout;

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();
    // try stdout.print("hey\n", .{});

    var testcases_file = try std.fs.cwd().openFile("./2015/day04/test.txt", .{});
    defer testcases_file.close();
    var testcase_reader = testcases_file.reader();

    const test_cases = try read_and_split(allocator, testcase_reader, "\n", "\r");
    defer {
        for (test_cases) |e| {
            allocator.free(e);
        }
        allocator.free(test_cases);
    }

    var file = try std.fs.cwd().openFile("./2015/day04/inp.txt", .{});
    defer file.close();
    var reader = file.reader();

    const inputs = try read_and_split(allocator, reader, "\n", "\r");
    defer {
        for (inputs) |e| {
            allocator.free(e);
        }
        allocator.free(inputs);
    }

    const p1 = try run_part([]const u8, part1, allocator, test_cases, &[_]isize{ 609043, 1048970 }, inputs[0]);
    _ = p1;

    // try stdout.print("part1={}\n", .{p1});

    // const p2 = try run_part([]const u8, part2, allocator, test_cases, &[_]isize{ 3, 11 }, inputs[0]);

    // try stdout.print("part1={}\n", .{p2});
}
