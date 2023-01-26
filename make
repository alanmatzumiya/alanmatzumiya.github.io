#!/usr/bin/env bash


Option=$1
Login=$( head $HOME/login )
Host=$( hostname -I )
Port="5000"

appPath=./app
Venv=venv/bin/activate
Reqs=requirements.txt

cvPath=./assets/portfolio/resume


function InstallServe () {
    
    echo "$Login" | sudo -S apt-get install ruby
    echo "$Login" | sudo -S apt-get install jekyll
    echo "$Login" | sudo -S apt-get install bundler

    echo "$Login" | sudo -S gem install jekyll bundler
    echo "$Login" | sudo -S gem install update    

    echo "$Login" | sudo -S bundle install
    echo "$Login" | sudo -S bundler install
    
}

function RunServe () {

    bundle exec jekyll serve -l -o -H [ --host $Host --port $Port ]
    
}

function InstallTex() {

    echo "$Login" | sudo -S apt-get install texlive-full

}

function BuildPortfolio () {
    
    cd $cvPath/templates && pdflatex main.tex && mv main.pdf ../cv.pdf
    for i in aux log out
    do
        rm "main.$i"
    done

}

function InstallApp () {       
    
    if ! [ -d ./app/venv ]; then
    
        cd ./app && virtualenv venv
        source ./$Venv && pip install -r ./$Reqs
        
    elif [[ -f ./app/$Reqs ]]; then

        cd ./app && source ./$Venv && pip install -r ./$Reqs
        
    fi
    
}

function RunApp () {
    
    cd ./app && source ./$Venv && python3 app.py
    
}


if [ $Option == "run-serve" ]; then
    (RunServe)
elif [ $Option == "install-serve" ]; then
    (InstallServe)
elif [ $Option == "run-app" ]; then
    (RunApp)
elif [ $Option == "install-app" ]; then
    (InstallApp)
fi;
