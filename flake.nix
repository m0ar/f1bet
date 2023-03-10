{
  description = "F1 betting visualiser";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        # packages.default = resha;
        devShells.default = with pkgs; mkShell {
          buildInputs = with python310Packages; [
            csvkit pandas matplotlib scipy jupytext
          ];
        };
      }
    );
}
