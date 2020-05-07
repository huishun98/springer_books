#!/bin/bash

curr_dir=$(PWD)
flask_dir_name="flask"
flask_dir="$curr_dir/$flask_dir_name"

cd $curr_dir

if [[ ! "$(python3 -V)" =~ "Python 3" ]]
then
    tput setaf 1
    echo "Please download Python at https://www.python.org/"
    exit 1
fi

pip install virtualenv

if [ "$(uname)" == "Darwin" ] 
then
    # Do something under Mac OS X platform      
    open http://localhost:8080/
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]
then
#     # Do something under GNU/Linux platform
    xdg-open http://localhost:8080/
else
    # Do something under 64 bits Windows NT platform
    start http://localhost:8080/
fi

virtualenv env
source env/bin/activate
pip install -r requirements.txt

cd $flask_dir
env FLASK_APP=deploy.py python -m flask run
