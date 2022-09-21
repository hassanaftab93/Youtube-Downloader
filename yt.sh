#!/bin/sh

# This shell script executes the python file
# This is to make the python file executable
chmod u+x ./src/download.py

python -m venv venv

source ./venv/bin/activate
source venv/Scripts/activate

pip install -r requirements.txt
python -m pip install --upgrade pytube
python -m pip install git+https://github.com/pytube/pytube

echo "Please Enter a Valid Youtube Video Link or Press CTRL+C to Exit: "
echo ""
read url_input

python ./src/download.py "$url_input"