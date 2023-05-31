#!/usr/bin/env bash

Option=$1
Login=$( head $HOME/login )
Host=$( hostname -I | awk '{print $1}' )
Host=$( python3 -c "from subprocess import getoutput as gout;print(gout('hostname -I').split()[-1])" )
Port="5000"
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

    bundle exec jekyll serve -l -H [ --host $Host --port $Port ]
    
}

function RunBuild () {

    Login=$( head $HOME/login )
    echo "$Login" | sudo -S bundle exec jekyll build JEKYLL_ENV=development -w -d /var/www/circuitalminds/contact/portfolio

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
    
        cd ./app && virtualenv venv && source ./venv/bin/activate && pip install -r ./requirements.txt
        
    elif [[ -f ./app/requirements.txt ]]; then

        cd ./app && source ./venv/bin/activate && pip install -r ./requirements.txt
        
    fi
    
}

function RunApp () {
    
    cd ./app && source ./venv/bin/activate && python3 app.py
    
}


if [ $Option == "run-serve" ]; then
    (RunServe)
elif [ $Option == "run-build" ]; then
    (RunBuild)
elif [ $Option == "install-serve" ]; then
    (InstallServe)
elif [ $Option == "run-app" ]; then
    (RunApp)
elif [ $Option == "install-app" ]; then
    (InstallApp)
fi;
