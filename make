#!/usr/bin/env bash


Option=$1
Login=$( python3 ./app/get-data.py login )
Host=$( python3 ./app/get-data.py host )
Port="5000"

function Backup () {
    topath="$HOME/Downloads"
    cd ./_site && cp -r ./* $topath
}

function RunServe () {
    if [ -d ./.jekyll-cache ]; then
        echo "$Login" | sudo -S rm -R ./.jekyll-cache
    fi
    for filename in .jekyll-metadata Gemfile.lock
    do
        if [ -f ./$filename ]; then
            echo "$Login" | sudo -S rm ./$filename
        fi
    done
    bundle exec jekyll serve -l -H --trace --incremental [ --host $Host --port $Port ]
}

function RunBuild () {
    Login=$( head $HOME/login )
    echo "$Login" | sudo -S bundle exec jekyll build --trace --incremental JEKYLL_ENV=development
}

function RunApp () {
    cd ./app && source ./venv/bin/activate && python3 app.py
}


if [[ $Option == "run-serve" ]]; then
    (RunServe)
elif [[ $Option == "run-build" ]]; then
    (RunBuild)
elif [[ $Option == "run-app" ]]; then
    (RunApp)
fi