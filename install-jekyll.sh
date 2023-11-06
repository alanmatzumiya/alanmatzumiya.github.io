#!/usr/bin/env bash

Host="192.168.1.4"
Port="5000"

sudo apt-get install ruby
sudo apt-get install jekyll
sudo apt-get install bundler

sudo gem install jekyll bundler
sudo gem install update    

bundle install
bundler install

bundle exec jekyll server -l -H [ --host $Host --port $Port ]
bundler exec jekyll server -l -H [ --host $Host --port $Port ]

