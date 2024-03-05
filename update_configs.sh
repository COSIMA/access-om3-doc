#!/usr/bin/env sh

set -e  # exit on error

# for each submodule, check out branch specfied in .gitmodules
git submodule foreach 'git checkout `git config -f "$toplevel/.gitmodules" --get submodule.$name.branch`'

# do git pull for each submodule
git submodule foreach 'git pull'
