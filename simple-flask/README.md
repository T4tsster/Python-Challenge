# Simple Todo app with Flask

## What to learn
- Start a simple CRUD Flask app
- Jinja2 syntax for frontend
- Init simple sqlite db
- Deploy to heroku

## Step-by-step command
Create virtural env
```
virtualenv flask
```

Activate env:
```
flask\Scripts\activate
```

Install environment:
```
pip install flask flask-sqlalchemy
```

Create sqlite database, open python shell:
```
from app import db
db.create_all()
```
This code can be included in script

## Deploy to Heroku

- Create & signin account on Heroku
- Download & install Heroku CLI

Start command to deploy:
```
heroku login

pip freeze > requirement.txt

git init
git add .

git commit -m ""

heroku create flask-crud-app

git push heroku master
```

Remember to add **Procfile** to tell Heroku what main file
