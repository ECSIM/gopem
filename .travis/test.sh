#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
 set -e
 set -x
 IS_IN_TRAVIS=false
 PYTHON_COMMAND=python
  
 if [ "$TRAVIS_OS_NAME" == "osx" ]
 then
	PYTHON_COMMAND=python3
 fi
 
 if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
 then
      IS_IN_TRAVIS=true
 fi
 $PYTHON_COMMAND -m gopem --test
 if [ "$IS_IN_TRAVIS" = 'false' ] || [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
 then
     $PYTHON_COMMAND -m vulture gopem/ rsrc/ setup.py --min-confidence 65 --sort-by-size
	 $PYTHON_COMMAND -m bandit -r gopem -s B322
	 $PYTHON_COMMAND rsrc/version_check.py
	 $PYTHON_COMMAND -m pydocstyle
 fi