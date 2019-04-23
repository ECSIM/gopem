#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
 set -e
 set -x
 if [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
 then
     python -m vulture --min-confidence 80 --exclude=gopem,build,.eggs --sort-by-size .
	 python -m bandit -r gopem -s B322
	 python version_check.py
 fi