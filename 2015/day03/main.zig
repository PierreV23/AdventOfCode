const std = @import("std");
const Allocator = std.mem.Allocator;
const ArrayList = std.ArrayList;
const Reader = std.fs.File.Reader;
const aoclib = @import("aoclib");
const read_and_split = aoclib.read_and_split;
const run_part = aoclib.run_part;

fn part1(allocator: Allocator, input: []const u8) anyerror!?isize {
    var map = std.AutoHashMap([2]isize, void).init(allocator);
    defer map.deinit();
    var y: isize = 0;
    var x: isize = 0;
    try map.put([_]isize{ y, x }, {});
    for (input) |char| {
        switch (char) {
            '^' => y -= 1,
            'v' => y += 1,
            '>' => x -= 1,
            '<' => x += 1,
            else => return error.UnknownSymbol,
        }
        try map.put([_]isize{ y, x }, {});
    }
    return map.count();
}

fn part2(allocator: Allocator, input: []const u8) anyerror!?isize {
    var map = std.AutoHashMap([2]isize, void).init(allocator);
    defer map.deinit();
    var sy: isize = 0;
    var sx: isize = 0;
    var ry: isize = 0;
    var rx: isize = 0;
    try map.put([_]isize{ 0, 0 }, {});
    var y: isize = 0;
    var x: isize = 0;
    var santas_turn = true;
    for (input) |char| {
        y = 0;
        x = 0;
        switch (char) {
            '^' => y = -1,
            'v' => y = 1,
            '>' => x = 1,
            '<' => x = -1,
            else => return error.UnknownSymbol,
        }
        if (santas_turn) {
            sy += y;
            sx += x;
        } else {
            ry += y;
            rx += x;
        }
        try map.put([_]isize{ sy, sx }, {});
        try map.put([_]isize{ ry, rx }, {});
        santas_turn = !santas_turn;
    }
    return map.count();
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();
    // try stdout.print("hey\n", .{});

    var testcases_file = try std.fs.cwd().openFile("./2015/day03/test.txt", .{});
    defer testcases_file.close();
    var testcase_reader = testcases_file.reader();

    const test_cases = try read_and_split(allocator, testcase_reader, "\n", "\r");
    defer {
        for (test_cases) |e| {
            allocator.free(e);
        }
        allocator.free(test_cases);
    }

    var file = try std.fs.cwd().openFile("./2015/day03/inp.txt", .{});
    defer file.close();
    var reader = file.reader();

    const inputs = try read_and_split(allocator, reader, "\n", "\r");
    defer {
        for (inputs) |e| {
            allocator.free(e);
        }
        allocator.free(inputs);
    }

    const p1 = try run_part([]const u8, part1, allocator, test_cases, &[_]isize{ 4, 2 }, inputs[0]);

    try stdout.print("part1={}\n", .{p1});

    const p2 = try run_part([]const u8, part2, allocator, test_cases, &[_]isize{ 3, 11 }, inputs[0]);

    try stdout.print("part1={}\n", .{p2});
}
