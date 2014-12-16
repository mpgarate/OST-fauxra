# fauxra

Accessible at http://fauxra.herokuapp.com

## How to test this assignment

You can browse fauxra.herokuapp.com to test this Q and A forum. 

Questions on the home page are sorted by recent activity, determined by 
whenever a question is updated. This occurs when created, edited, answered,
or voted on, as well as when one of its answers is edited or voted on. 

1. Multiple Users: User authentication is handled in the upper right 
on the navbar. If you try to perform some action that requires auth, you will
be redirected to a login page. This page also has a link to registration. 

2. A user can create and edit both questions and answers. Create a qustion with 
green button on the home page, and add an answer to a question with the green button
below every question. If you are the author of a question, you will see an 
“edit question” link in the upper right of the blue question window. Similarly, 
the creator of an answer can see an Edit answer button in the upper right of
the grey answer window. 

3. Pagination can be observed on the home page at the bottom when there are 
more than 10 items.

4. When viewing a question, answers are sorted based on their vote score. 

5. When creating and editing a question, tags can be set. When viewing a question,
clicking on a tag will bring you to an index for all questions matching that tag. 

6. URLs are changed into anchor tags and images into embedded images. 
This only occurs when you are viewing a question. 
Example with URLS: http://fauxra.herokuapp.com/questions/3/
Example with images: http://fauxra.herokuapp.com/questions/12/

7. Images can browsed by permalinks and uploaded from:
http://fauxra.herokuapp.com/images/

8. Question text on the home page is capped at 500 characters. You will notice
a question with a very long title demonstrating this feature. 

9. These timestamps can be seen on a view question page in the following locations:
Question create date - in the blue bar on the top
Question edit date - on the lower right of the blue box
Answer create date - in the grey bar above the question
Answer edit date - in the lower right corner of the answer (only appears if edited)

10. The home page contains a link to an RSS feed at the bottom which contains
references to recent questions. When viewing a question, there is also a link
to the Answers RSS feed. 

11. I created a git branch named remove_rss which has the tag “experiment”

## How this project is designed

This project uses the django framework with a postgres database, the heroku 
cloudinary service for image handling and taggit for tag management.
Also, I used Bootstrap to help with styling the website. 
I used the following python packages:

dj-database-url==0.3.0
dj-static==0.0.6
django-registration==1.0
django-taggit==0.12.2
django-toolbelt==0.0.1
gunicorn==19.1.1
psycopg2==2.5.4
six==1.8.0
static3==0.5.1

The root folder contains directories for various modules detailed below:
In general, the modules are designed to be independent and reusable. 
In hindsight, the questions module got pretty big and it may have been worth
splitting answers into a separate module or submodule. 

fauxra: the primary module for this django setup. 
  urls.py - defines the project-wide handlers for url paths
  settings.py - configure use of other modules and modes for this project
questions: the module containing the core functionality around questions and answers
  models.py - define the classes for q and a
  views.py - define the view handlers for q and a routes
  urls.py - define which views connect with which url paths
  templates/ - contains html template files
  templatetags/filters.py - define filters to use in templates for rewriting img/urls
accounts: handle user registration and authentication
  no models because django user models used instead
  urls.py - auth url definitions
  views.py - auth views
  templates/ - template files
images: support uploading and displaying images
  models.py - image classes
  views.py - image views
  urls.py - image url definitions
  templates/ - template files


Also, the database configuration is done by environment variables using the format:
export DATABASE_URL=postgres://fauxra:password@localhost/fauxra


## How to run locally
Set up a virtualenv with the following command:

when creating a venv, use the following command:
```sh
virtualenv venv --no-site-packages
```

Configure a postgres database. I referenced this guide: 
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn


Inside the virtualenv, clone this repository and then run
```sh
source /opt/myenv/bin/activate
```

Then, install required packages with 
```sh
pip install -r requirements.txt
```

Finally, sync/migrate the database and start the server with:
```sh
./manage.py syncdb
./manage.py runserver
```

And visit `http://localhost:8000/` in your browser. 

Heroku will run instead with the command:
```sh
foreman start
```

Manage dependencies with:

```sh
pip freeze > requirements.txt
pip install -r requirements.txt
```

When extending models in this app, make sure to migrate the db locally and on heroku
```sh
./manage.py makemigrations
./manage.py migrate
```

Run migrations on Heroku with:
```sh
heroku run python manage.py migrate
```

