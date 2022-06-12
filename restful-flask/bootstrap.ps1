#!/bin/sh
$env:FLASK_APP = "./cashman/index.py"
$env:FLASK_ENV = "development"
conda activate Flask 
flask run