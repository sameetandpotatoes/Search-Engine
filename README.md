## Installation

- `git clone https://github.com/sameetandpotatoes/Search-Engine.git searchengine`
- `cd searchengine`

If you have a Mac, you probably already have pip installed, but just check/upgrade first:

    pip install -U pip setuptools

We are using a `virtualenv` in Python to use self-contained, independent python packages
so that we don't have any version conflicts. This means that whenever you want to run,
test, or do anything, you must be in the virtualenv.

## Postgres Installation

- http://postgresapp.com
- Install, make sure it's running before you start the application (see the elephant in your menu bar at the top)

## `virtualenv` Installation

- `virtualenv dev` (You don't have to call it dev, but I will for the remainder of this; it's just the name of your environment).
- `source dev/bin/activate`

Now that you are inside the virtual environment, install all of your packages inside of it from the `requirements.txt`:

    pip install -r requirements.txt

## Compiling JavaScript

- Have [npm](https://nodejs.org/en/) installed.
- Run `npm install` in the project root.
- Then run `npm start`. Note that this is a perpetual task and if you cancel it, your JS changes will not show when you refresh the browser.
- Now all JS changes will automatically (in a few seconds) get compiled down to `js` in `static/js`

## Installing ElastiSearch

After [downloading](https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/zip/elasticsearch/2.0.0/elasticsearch-2.0.0.zip) the latest release and extracting it, elasticsearch can be started using:

    bin/elasticsearch

Make sure that [http://localhost:9200](http://localhost:9200) opens up and shows you some json. That's how you know it's running!

## Database Setup

- Set up your PATH correctly:

- In `~/.bash_profile`, add:

        export PATH="/Applications/Postgres.app/Contents/Version/9.4/bin:$PATH"

- Then run `source ~/.bash_profile`

- Run these commands in Terminal:

        createdb searchengine
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

## Making Migrations

- If you make a change in `engine/models.py`, you need to migrate those changes to the database schema. Do that with:

        python manage.py makemigrations && python manage.py migrate

Now, in a separate window/tab in your Terminal, you can finally run:

      python manage.py runserver

Open up `http://localhost:8000`!


## ElastiSearch index updating:

Using the standard SearchIndex, your search index content is only updated whenever you run either `python manage.py update_index` or start afresh with `python manage.py rebuild_index`.
