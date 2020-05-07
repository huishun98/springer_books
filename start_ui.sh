#!/bin/bash
curr_dir=$(PWD)
ui_dir_name="ui_download"
ui_dir="$curr_dir/$ui_dir_name"

cd $ui_dir



if which node > /dev/null
then
    npm install -g @vue/cli
    npm run build
    npm run serve
else
    tput setaf 1
    echo 'Please download Node.js from https://nodejs.org/en/'
fi

$SHELL