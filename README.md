# fauxra

Questions on the home page are sorted by recent activity, determined by 
whenever a question is updated. This occurs when created, edited, answered,
or voted on, as well as when one of its answers is edited or voted on. 

Run locally with:
```sh
./manage.py runserver
```

Heroku runs with:
```sh
foreman start
```

Run migrations on Heroku with:
```sh
heroku run python manage.py migrate
```

Manage dependencies with:

```sh
pip freeze > requirements.txt
pip install -r requirements.txt
```

when creating a venv, use the following command:
```sh
virtualenv venv --no-site-packages
```
