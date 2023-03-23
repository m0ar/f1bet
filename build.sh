#! /bin/env bash

set -eo pipefail
NB_SCRIPT="src/f1_display_2023.py"

mkdir -p figs
jupytext src/f1_display_2023.ipynb --to=script --quiet
HEADLESS=true FIG_OUTPUT_DIR=figs python "$NB_SCRIPT" > /dev/null
rm "$NB_SCRIPT"

mkdir -p dist
cp src/style.css dist

cat > dist/index.html <<EOF
<html>
<head>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class='gallery'>
EOF

for fig in figs/*; do
  data="$(base64 $fig)"
  echo "<img src='data:image/png;base64,$data'>" >> dist/index.html
done

cat >> dist/index.html <<EOF
</div>
</body>
</html>
EOF
