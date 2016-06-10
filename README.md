
# UNCHAINED

Unchained is not a framework. It is a _very_ opionated Flask app that takes things from Django the authored liked and ignored  

## CLONING

Nothing surprising, make sure you have access to the repo:

    $ git clone git@github.com:ZXVentures/bi-dw.git


## INSTALL

Create your virtual environment:

    $ virtualenv -p python3 bi-dw-env

If you don't have virtualenv installed:

    $ sudo pip install virtualenv

You will probably want to upgrade to the latest pip

    $ pip install --upgrade pip

	
## ACTIVATE

    $ source bi-dw-env/bin/activate 

You can deactivate this by typing `deactivate`


## BUILDING

    $ pip install -r requirements/dev.txt   
    $ ./manage db upgrade
    $ ./manage.py seed

Note that if you're using the sqlite database, it doesn't support ALTER TABLE so any migrations that alter a table's structure will silently fail.

## MIGRATIONS

As suggested in the previous section, we are using a migration library to manage the migration of the database, triggers, etc. Like in Django, when you make a change to a model you will need to create the migration that describes the changes:

    $ ./manage.py db migrate

You should physically look at the migration script to ensure it makes sense. Once you're happy with it, you can run it on the database:

    $ ./manage.py db upgrade

## PEP8 Compliance

We're more or less PEP8 compliant, some things we really care about (which is to say Python cares as well):

    * Use spaces, not tabs
    * Indent 4 spaces

You can test your code's compliance with:

    $ pep8 some/file/or/dir


## TESTING

See _important_ note below about how to run the debugger with nose.

To run the test suite:

    $ ./manage.py test

Or just a file:

    $ ./manage.py test tests/test_app.py

Or just a Class in a file:

    $ ./manage.py test tests/test_app.py:TestApp

Or a test in a Class:

    $ ./manage.py test tests/test_app.py:TestApp.test_the_testing

Note there is a lot granularity in running tests, read: https://pythonhosted.org/Flask-Testing/


## RUNNING THE WEB SERVER

    $ ./manage.py runserver


## DEBUGGING

You will need `nose` to drop into the pdb console with `-s`:

    $ ./manage.py test -s tests/test_reports.py

