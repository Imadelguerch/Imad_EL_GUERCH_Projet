#!/bin/bash
source .env/bin/activate
pip3 install -r requirements.txt
pip freeze > requirements.txt
python main.py

