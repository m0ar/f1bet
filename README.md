# F1 bet visualiser
This repo holds Jesper Browall's excellent F1 bet visualiser,
modified for headless execution to generate plots, and wrappers
to generate static HTML content from them.

## Dependencies
Install [Nix](https://nixos.org/download.html), then run `nix develop`
in the repo root and all dependencies are automatically available.

## Building
Run `./build.sh` to generate figures and HTML content in `/figs` and
`/dist`, respectively. The figures are already embedded as raw base64
data in the HTML.

### How it works
The build script uses [`jupytext`](https://github.com/mwouts/jupytext) to
convert the `.ipynb` file to a regular Python script. This is run with the
new configuration variables `HEADLESS=true` and `FIG_OUTPUT_DIR=figs`, which
overrides showing the `pyplot` windows and instead saves the files to disk.

The raw data of these files is converted to [base64](https://en.wikipedia.org/wiki/Base64)
and put into `img` tags using `data` URLs inside a simple boilerplate HTML
document with reactive gallery style CSS.

## Deployment
This is done automatically on push to the master branch.
Do do it manually, run `wrangler publish dist --project=f1bet`
(requires authentication).

