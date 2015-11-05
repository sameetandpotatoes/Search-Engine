## Installation

- `git clone https://github.com/sameetandpotatoes/Search-Engine.git searchengine`
- `cd searchengine`

If you have a Mac, you probably already have pip installed, but just check/upgrade first:

    pip install -U pip setuptools

- `pip install -r requirements.txt`

We are using a `virtualenv` in Python to use self-contained, independent python packages
so that we don't have any version conflicts. This means that whenever you want to run,
test, or do anything, you must be in the virtualenv. You can do that with this command:

- `source dev/bin/activate` (dev is the name of the virtual environment)

Now, finally you can run:

- `python manage.py runserver`
