#!/usr/bin/env bash

Option=$1
Login=$( head $HOME/login )
Host=$( python3 ./app/get-data.py host )
Port="5000"


function RunServe () {

    if [ -d ./.jekyll-cache ]; then
        rm -R ./.jekyll-cache
    fi
    
    for filename in .jekyll-metadata Gemfile.lock
    do
        if [ -f ./$filename ]; then
            rm ./$filename
        fi
    done

    bundle exec jekyll serve -l -H [ --host $Host --port $Port ]
    
}

function RunBuild () {

    Login=$( head $HOME/login )
    echo "$Login" | sudo -S bundle exec jekyll build --trace --incremental JEKYLL_ENV=development

}

function RunCopy () {

    topath="$HOME/GitHub/circuitalminds/circuitalminds.github.io/_includes/page/portfolio"
    cd ./_site && cp -r ./* $topath

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
elif [ $Option == "run-copy" ]; then
    (RunCopy)
fi
