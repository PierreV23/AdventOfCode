const std = @import("std");
const Allocator = std.mem.Allocator;
const ArrayList = std.ArrayList;
const Reader = std.fs.File.Reader;
const aoclib = @import("aoclib");
const read_and_split = aoclib.read_and_split;
const run_part = aoclib.run_part;
const Md5 = std.crypto.hash.Md5;

const Options = struct {
    part: aoclib.Part = .one,
};

fn is_nice_p1(input: []const u8) bool {
    var prev_char: u8 = '.';
    var nice = true;
    var vowels: usize = 0;
    var was_twice = false;
    for (input) |char| {
        if (!nice) break;
        if (std.mem.containsAtLeast(u8, "aeiou", 1, &[_]u8{char})) vowels += 1;
        if (prev_char == char) was_twice = true;
        if (std.mem.containsAtLeast(u8, "ab,cd,pq,xy", 1, &[_]u8{ prev_char, char })) nice = false;
        prev_char = char;
    }
    nice = nice and was_twice and vowels >= 3;
    return nice;
}

fn is_nice_p2(allocator: Allocator, input: []const u8) !bool {
    var prev_chars: [2]u8 = "..".*;
    var nice = true;
    var map = std.AutoHashMap([2]u8, usize).init(allocator);
    defer map.deinit();
    var had_triple = false;
    var had_pair_twice = false;
    for (input, 0..) |char, idx| {
        if (!nice) break;
        if (prev_chars[0] == char) had_triple = true;
        // try std.fmt.bufPrint(&prev_chars, "{c}{c}", .{ prev_chars[1], char });
        prev_chars = [2]u8{ prev_chars[1], char };
        if (!had_pair_twice) {
            if (map.contains(prev_chars)) {
                had_pair_twice = map.get(prev_chars).? != idx - 1;
            } else {
                try map.put(prev_chars, idx);
            }
        }
    }
    nice = had_triple and had_pair_twice;
    return nice;
}

fn part1(lines: [][]const u8) usize {
    var count: usize = 0;
    for (lines) |line| count += @intFromBool(is_nice_p1(line));
    return count;
}

fn part2(allocator: Allocator, lines: [][]const u8) !usize {
    var count: usize = 0;
    for (lines) |line| count += @intFromBool(try is_nice_p2(allocator, line));
    return count;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

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

    var file = try std.fs.cwd().openFile("./2015/day05/inp.txt", .{});
    defer file.close();
    var reader = file.reader();

    const inputs = try read_and_split(allocator, reader, "\n", "\r");
    defer {
        for (inputs) |e| {
            allocator.free(e);
        }
        allocator.free(inputs);
    }

    const p1 = part1(inputs);

    try stdout.print("part1={}\n", .{p1});

    const p2 = try part2(allocator, inputs);

    try stdout.print("part2={}\n", .{p2});
}
