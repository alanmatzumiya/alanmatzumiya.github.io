#!/usr/bin/env bash

Option=$1
Login=$( head $HOME/login )
Host=$( python3 ./app/get-data.py host )
Port="5000"


function RunServe () {

    bundle exec jekyll serve -l -H [ --host $Host --port $Port ]
    
}

function RunBuild () {

    Login=$( head $HOME/login )
    echo "$Login" | sudo -S bundle exec jekyll build JEKYLL_ENV=development -w -d /var/www/circuitalminds/contact/portfolio

}

function RunApp () {
    
    cd ./app && source ./venv/bin/activate && python3 app.py
    
}


if [ $Option == "run-serve" ]; then
    (RunServe)
elif [ $Option == "run-build" ]; then
    (RunBuild)
elif [ $Option == "run-app" ]; then
    (RunApp)
fi;
