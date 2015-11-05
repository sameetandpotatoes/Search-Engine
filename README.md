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

Now, finally you can run:

- `python manage.py runserver`
