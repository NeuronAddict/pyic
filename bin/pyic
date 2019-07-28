#!/usr/bin/env bash

FILE=$(mktemp)
cat <<EOF ${1} >> ${FILE}
from pyic import *
EOF
python3 -i ${FILE}
