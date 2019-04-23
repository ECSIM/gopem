#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
set -e
set -x

python -m bandit -r gopem -s B322
python -m vulture --min-confidence 80 --exclude=gopem,build,.eggs --sort-by-size .