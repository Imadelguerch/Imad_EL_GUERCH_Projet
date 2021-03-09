#!/bin/bash
python3 -m venv .env
activate () {
	.  ./.env/bin/activate
}

activate
pip3 install -r requirements.txt
pip freeze > requirements.txt
python main.py
