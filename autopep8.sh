#!/bin/bash
python -m autopep8 gopem --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose
python -m autopep8 setup.py --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose
python -m autopep8 rsrc --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose