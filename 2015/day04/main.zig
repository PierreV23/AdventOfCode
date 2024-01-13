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

fn solver(allocator: Allocator, input: []const u8, options: Options) anyerror!?isize {
    var count: isize = 10;
    var as_hex = ArrayList(u8).init(allocator);
    defer as_hex.deinit();
    var buf: [Md5.digest_length]u8 = undefined;
    var wzp_buf: [16 + 10]u8 = undefined;
    while (true) {
        as_hex.clearRetainingCapacity();
        buf = undefined;
        wzp_buf = undefined;
        const wzp = try std.fmt.bufPrint(&buf, "{s}{}", .{ input, count });
        Md5.hash(wzp, &buf, .{});
        try std.fmt.fmtSliceHexLower(&buf).format("{}", .{}, as_hex.writer());
        if (std.mem.startsWith(u8, as_hex.items, if (options.part == .one) "00000" else "000000")) {
            break;
        }
        count += 1;
    }
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

    // const p1 = try run_part([]const u8, part1, allocator, test_cases, &[_]isize{ 609043, 1048970 }, inputs[0]);
    const p1 = try solver(allocator, inputs[0], .{});

    try stdout.print("part1={}\n", .{p1.?});

    const p2 = try solver(allocator, inputs[0], .{ .part = .two });

    try stdout.print("part2={}\n", .{p2.?});
}
