## Installation

- `git clone https://github.com/sameetandpotatoes/Search-Engine.git searchengine`
- `cd searchengine`

If you have a Mac, you probably already have pip installed, but just check/upgrade first:

    pip install -U pip setuptools

We are using a `virtualenv` in Python to use self-contained, independent python packages
so that we don't have any version conflicts. This means that whenever you want to run,
test, or do anything, you must be in the virtualenv.

## `virtualenv` Installation

- `virtualenv dev` (You don't have to call it dev, but I will for the remainder of this; it's just the name of your environment).
- `source dev/bin/activate`

Now that you are inside the virtual environment, install all of your packages inside of it from the `requirements.txt`:

- `pip install -r requirements.txt`

## Postgres Installation

- [http://www.postgresql.org/download/](http://www.postgresql.org/download/)
- Install, make sure it's running before you start the application

## Compiling JavaScript

- Have `npm` installed.
- Run `npm install`
- Then run `npm start`. Note that this is a perpetual task and if you cancel it, your JS changes will not show when you refresh the browser.
- Now all JS changes will automatically (in a few seconds) get compiled down to `js` in `static/js`

### Database Setup

- With postgres, run these commands

    psql
    CREATE DATABASE searchengine
    Ctrl + D to exit
    createuser -P -s -e cook
    Enter `chef` as the password

- In the searchengine folder, create a file called `local_settings.py`:

    DEBUG = True
    TEMPLATE_DEBUG = True

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "searchengine",
            "USER": "cook",
            "PASSWORD": "chef",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }

Check that everything works by running:

    python manage.py syncdb && python manage.py makemigrations && python manage.py migrate

If it does, you're set and you can run the local server. If not, reach out to me and I'll see if I can help.

### Making Migrations

- If you make a change in `engine/models.py`, you need to migrate those changes to the database schema. Do that with:

    python manage.py makemigrations engine


Now, in a separate window/tab in your Terminal, you can finally run:

- `python manage.py runserver`
