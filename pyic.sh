#!/usr/bin/env bash

if [[ -d pyic ]]
then
    echo "Please launch me on the pyic dir (not pyic/pysqli)"
    exit 0
fi

FILE=$(mktemp)

cat ./pysqli/__init__.py ${1} >> ${FILE}

export PYTHONPATH="$PYTHONPATH:."
python3 -i ${FILE}
