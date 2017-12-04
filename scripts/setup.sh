#!/bin/bash

# Set up folders and files for each AoC day

# I could use bracket expansion to Bash-Golf it to one or two lines,
# but it makes it tricky to revise. So lame way it is.

day=$1
case ${day#[-+]} in
  *[!0-9]* | '') echo Not a valid day number; exit 1;;
  * ) ;;
esac
echo "Making folder and file structure for Day ${day?}"
mkdir day"${day?}"
touch day"${day?}"/README.md
touch day"${day?}"/input.txt
touch day"${day?}"/solution.py
touch day"${day?}"/solution2.py
chmod +x day"${day?}"/solution.py
chmod +x day"${day?}"/solution2.py
echo "Done"
