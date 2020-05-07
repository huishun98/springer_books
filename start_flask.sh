#!/bin/bash

curr_dir=$(PWD)
flask_dir_name="flask"
flask_dir="$curr_dir/$flask_dir_name"

open http://localhost:8080/


cd $curr_dir
source env/bin/activate
pip install -r requirements.txt

cd $flask_dir
env FLASK_APP=deploy.py python -m flask run
