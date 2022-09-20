#!/bin/sh

# This shell script executes the python file
# This is to make the python file executable
chmod u+x ./src/download.py

echo "Please Enter a Valid Youtube Video Link or Press CTRL+C to Exit: "
echo ""
read url_input

python ./src/download.py "$url_input"