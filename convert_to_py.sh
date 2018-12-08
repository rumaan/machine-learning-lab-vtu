#!/bin/bash/env bash
#
# Script Name: convert_to_py.sh
#
# Author: rumaan
# Date: 08/12/2018
#
# Description: This script converts the Jupyter ipynb files into python scripts
#              and sanitzes them.

# Check if jupyter is installed
if ! type "jupyter" > /dev/null 2>&1; then
    echo "Error: Jupyter isn't installed!"
    exit 1
fi

# TODO: Check if nbconvert is installed
# if ! type "jupyter nbconvert" > /dev/null 2>&1; then
#     echo "Error: nbconvert not installed!"
#     echo "Try: pip install nbconvert"
#     exit 1
# fi

# Convert all the ipynb files in the current directory to .py
jupyter nbconvert *.ipynb --to script

# Move all the py files into ./py/ directory
echo "Creating py directory to save the .py files..."
mkdir -p py
echo "Moving .py files..."
mv *.py ./py
cd py

# Output for trimmed python files
echo "Creating trimmed directory..."
mkdir -p trimmed

# List of all the *.py files
files=`ls *py`
# Sanitize the py files
# Remove '# In []' lines
echo "Sanitizing Files..."
for f in *.py
do
    #filename=`cut -d. -f1 <<< "$file" | cut -c-2`.py
    echo "Processing $f..."
    sed -e '/# In/d' -e '/^$/d' "$f" > "./trimmed/$f"
done

# cut -d. -f1 <<< "filename.py" | cut -c-2
# filename=`cut -d. -f1 <<< $file | cut -c-2`
# filename+=".py"
echo "Successfully Converted Jupyter Notebook files into Python Scripts."
echo "All .py files are saved in ./py/trimmed/"