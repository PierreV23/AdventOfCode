{
  description = "Zig development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    zig-overlay.url = "github:mitchellh/zig-overlay";
    zls.url = "github:zigtools/zls?ref=0.15.0";
  };

  outputs = { self, nixpkgs, zig-overlay, zls, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
      zig = zig-overlay.packages.${system}."0.15.2";
      zls-pkg = zls.packages.${system}.zls.overrideAttrs (old: {
        nativeBuildInputs = [ zig ];
      });
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [ zig zls-pkg ];
        
        shellHook = ''
          echo "Zig ${zig.version} development environment"
          echo "ZLS language server available"
        '';
      };
    };
}
