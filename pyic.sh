#!/usr/bin/env bash

if [[ -d pyic ]]
then
    echo "Please launch me on the pyic dir (not pyic/pysqli)"
    exit 0
fi

export PYTHONSTARTUP=./pysqli/__init__.py
export PYTHONPATH="$PYTHONPATH:."
python3
