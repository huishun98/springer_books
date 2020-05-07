#!/bin/bash
curr_dir=$(PWD)
ui_dir_name="ui_download"
ui_dir="$curr_dir/$ui_dir_name"

cd $ui_dir

if which node > /dev/null
then
    npm run build
    npm run serve
else
    echo 'Please download Node.js'
    open https://nodejs.org/en/
fi
