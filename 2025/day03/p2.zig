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

        var ns: [12]u8 = undefined;

        var curr_idx_line: usize = 0;

        for (0..12) |ns_idx| {
            const offset = (12 - ns_idx - 1);
            const slice = line[curr_idx_line .. line.len - offset];
            const max_idx = util.maxIdx(slice).?;
            ns[ns_idx] = line[max_idx + curr_idx_line];
            curr_idx_line = max_idx + curr_idx_line + 1;
            // print("{s}, {}, {}, {}, {s}, {}, {c}\n", .{ line, ns_idx, max_idx, offset, slice, max_idx, line[max_idx] });
        }

        print("{s}\n", .{ns});
        count += try std.fmt.parseInt(u64, &ns, 10);
    }

    print("{}\n", .{count});
}
