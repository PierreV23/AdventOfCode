const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const util = b.addModule("util", .{
        .root_source_file = b.path("src/util.zig"),
    });

    const day_arg = b.option([]const u8, "day", "Day to run (e.g., day01/p1)") orelse "day01/p1";

    const exe = b.addExecutable(.{
        .name = "aoc",
        .root_module = b.createModule(.{
            .root_source_file = b.path(b.fmt("{s}.zig", .{day_arg})),
            .target = target,
            .optimize = optimize,
        }),
    });

    exe.root_module.addImport("util", util);
    b.installArtifact(exe);

    const run_cmd = b.addRunArtifact(exe);
    run_cmd.step.dependOn(b.getInstallStep());

    const run_step = b.step("run", "Run the app");
    run_step.dependOn(&run_cmd.step);
}
