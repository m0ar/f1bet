#! /bin/env bash

set -eo pipefail
NB_SCRIPT="src/f1_display_2023.py"

mkdir -p figs
jupytext src/f1_display_2023.ipynb --to=script
HEADLESS=true FIG_OUTPUT_DIR=figs python "$NB_SCRIPT" > /dev/null
rm "$NB_SCRIPT"

OUTFILE="dist/index.html"
mkdir -p "$(dirname $OUTFILE)"

cat > $OUTFILE <<EOF
<html>
<head>
<style>
.gallery {
  display: grid;
  width: 100vw;
  grid-auto-rows: 500px;
}
@media (min-width: 1200px) {
  .gallery { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1800px) {
  .gallery { grid-template-columns: repeat(3, 1fr); }
}
.gallery > img {
  width: 0;
  height: 0;
  min-height: 100%;
  min-width: 100%;
  object-fit: contain;
}

body {
  margin: 0;
}
</style>
</head>
<body>
<div class='gallery'>
EOF

for fig in figs/*; do
  data="$(base64 $fig)"
  echo "<img src='data:image/png;base64,$data'>" >> $OUTFILE
done

cat >> $OUTFILE <<EOF
</div>
</body>
</html>
EOF
