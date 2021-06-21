#!/bin/sh -l

echo "EXECUTING PYTHON SCRIPT..."
python3 /main.py

echo "ls -lah"
ls -lah

echo "pwd"
pwd

echo "ls -lah /github/workspace"
ls -lah /github/workspace

sudo chmod 655 log.md

sudo echo "Text1: ${{ github.event.inputs.text1 }}" >> log.md
