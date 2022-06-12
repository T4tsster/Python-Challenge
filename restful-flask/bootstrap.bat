#!/bin/sh
set "FLASK_APP=.\cashman\index.py"
conda activate Flask
flask run -h 0.0.0.0