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
        devShells.default = with pkgs; mkShell {
          buildInputs = [
            csvkit
            nodePackages.wrangler
          ] ++ (with python310Packages; [
            pandas
            matplotlib
            scipy
            jupytext
          ]);
        };
      }
    );
}
