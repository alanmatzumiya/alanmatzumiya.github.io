#!/usr/bin/env bash


if [ -d venv ]; then
    source ./venv/bin/activate && python3 app.py
fi
