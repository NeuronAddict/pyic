#!/usr/bin/env bash

if [[ -d pysqli ]]
then
    echo "Please launch me on the pysqli dir (not pysqli/pysqli)"
fi

export PYTHONSTARTUP=./pysqli/__init__.py
export PYTHONPATH="$PYTHONPATH:."
python3