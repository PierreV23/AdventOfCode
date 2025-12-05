// const util = @import("util");
// const std = @import("std");

// const print = @import("std").debug.print;
// pub fn sum(n: u64) u64 {
//     return (n * (n + 1) / 2);
// }

// pub fn getBelow(allocator: std.mem.Allocator, n1_string: []const u8) !u64 {
//     var string = n1_string;
//     var allocated_string: ?[]u8 = null;
//     defer if (allocated_string) |s| allocator.free(s);

//     if (string.len & 0b1 == 1) {
//         allocated_string = try allocator.alloc(u8, string.len - 1);
//         @memset(allocated_string.?, '9');
//         // print("old={s}", .{string});
//         string = allocated_string.?;
//         // print(" alloc={s} new={s} \n", .{ allocated_string.?, string });
//     }

//     const n1 = try std.fmt.parseInt(u64, string, 10);
//     const e = std.math.pow(u64, 10, string.len / 2);
//     var left = n1 / e;
//     const duped = left * e + left;
//     if (duped > n1) left -= 1;

//     print("{s} {s} {} {}\n", .{ n1_string, string, left, left });
//     // return left;
//     print("sum({}) * {} + sum({}) = {}; {}\n", .{ left, e, left, sum(left) * e + sum(left), sum(left) });
//     return sum(left) * e + sum(left);
// }

// pub fn main() !void {
//     var gpa = std.heap.GeneralPurposeAllocator(.{}){};
//     defer _ = gpa.deinit();

//     const allocator = gpa.allocator();

//     const text = try util.readUntilBlank(allocator);
//     defer allocator.free(text);

//     var lines = std.mem.splitScalar(u8, text, '\n');
//     const line = lines.next().?;

//     var ranges = std.mem.splitScalar(u8, line, ',');

//     var count: u64 = 0;
//     count = 0;

//     while (ranges.next()) |range| {
//         print("\n", .{});
//         var numbers = std.mem.splitScalar(u8, range, '-');
//         const n1_string = numbers.next().?;
//         const n1 = try std.fmt.parseInt(u64, n1_string, 10) - 1;
//         const n1_string_new = try std.fmt.allocPrint(allocator, "{}", .{n1});
//         defer allocator.free(n1_string_new);

//         const n2_string = numbers.next().?;

//         const n1_ans = try getBelow(allocator, n1_string_new);
//         const n2_ans = try getBelow(allocator, n2_string);

//         // print("{s}..{s}: {}-{}=", .{ n1_string, n2_string, n2_ans, n1_ans });
//         // print("{}\n", .{n2_ans - n1_ans});

//         print("{s}..{s} {}\n", .{ n1_string, n2_string, n2_ans - n1_ans });
//         count += n2_ans - n1_ans;

//         // const n2_string = try std.fmt.parseInt(u64, numbers.next().?, 10);

//         // for (n1..n2 + 1) |number| {
//         //     const string = try std.fmt.allocPrint(allocator, "{}", .{number});
//         //     defer allocator.free(string);

//         //     const len = string.len;

//         //     if (len & 0b1 == 1) continue;

//         //     if (std.mem.eql(u8, string[0 .. len / 2], string[len / 2 ..])) {
//         //         // print("{s} {s} {s}\n", .{ string, string[0 .. len / 2], string[len / 2 ..] });
//         //         count += number;
//         //     }
//         // }
//     }

//     print("{}\n", .{count});
// }

// i know what i'd have to do to make it work but im lazy

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
    const line = lines.next().?;

    var ranges = std.mem.splitScalar(u8, line, ',');

    var count: u64 = 0;
    count = 0;

    while (ranges.next()) |range| {
        var numbers = std.mem.splitScalar(u8, range, '-');

        const n1 = try std.fmt.parseInt(u64, numbers.next().?, 10);
        const n2 = try std.fmt.parseInt(u64, numbers.next().?, 10);

        for (n1..n2 + 1) |number| {
            const len = std.math.log10(number) + 1;

            if (!util.intIsEven(len)) continue;

            const t = std.math.pow(usize, 10, len / 2);

            const left = number / t;

            const new = left * t + left;

            // print("{} {} {}\n", .{ number, left, new });
            if (new == number) {
                count += number;
                print("{}\n", .{number});
            }
        }
    }

    print("{}\n", .{count});
}
