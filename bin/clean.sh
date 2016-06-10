#!/usr/bin/env bash
find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf
