#!/bin/bash
curr_dir=$(PWD)
ui_dir_name="ui"
ui_dir="$curr_dir/$ui_dir_name" 

cd $ui_dir
npm run build
npm run serve
