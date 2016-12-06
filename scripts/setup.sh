#!/bin/bash

# Set up folders and files for each AoC day

# I could use bracket expansion to Bash-Golf it to one or two lines,
# but it makes it tricky to revise. So lame way it is.

day=$1
echo "Making folder and file structure for Day $1"
mkdir day$1
touch day$1/README.md
touch day$1/input.txt
touch day$1/solution.py
touch day$1/solution2.py
chmod +x day$1/solution.py
chmod +x day$1/solution2.py
echo "Done"
