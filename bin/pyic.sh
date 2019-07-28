#!/usr/bin/env bash

FILE=$(mktemp)
cat <<EOF ${1} >> ${FILE}
from pysqli import *
EOF
python3 -i ${FILE}
