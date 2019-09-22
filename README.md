## Bank Search

    $ python manage.py runserver

The app will be served by django **runserver**

Access it through **http://localhost:8000**

## Setup of development environment

First install required dependencies.

After that, create your virtualenv (Can use Virtualenvwrapper and Pipenv):

    $ virtualenv -p python3.7 env
    
Activate virtualenv:

    $ source <path>/env/bin/activate

Install Requirements:

    $ pip install -r requirements.txt
    
Migrate:

    $ ./manage.py migrate
    
And to start the django dev server:

    $ ./manage.py runserver

## Version
* Python : 3.6+
* PostgreSql : 10+

