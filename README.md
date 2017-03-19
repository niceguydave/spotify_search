# Simple Spotify search

## Description
The following project allows a user to perform a simple search on 
Spotify information which exposed via its API.  

When user selects a filter and types a search term, a request is made
to the Spotify API

Spotify results are parsed and generate a page containing results

A "Counter" shows the count of the results returned.

Search results contain a 64x64 thumbnail beside them whenever 
available.

Data is paginated

## Notes
* For speed of development and due to the author's familiarity with the
framework, Django has been used to create this app.  A more lightweight
framework such as Flask on web.py would probably be more suitable for 
such a lightweight app and recreating this in such a framework would 
be a good future exercise.
* There are no tests with this project, which really is not a good thing
Given a little more time there are some basic tests which could
fairly quickly be integrated. 
* The Spotify API only returns a maximum of 50 items in any one call.
The next iteration of this design could take into account this 
limitation.


## Installation

This package uses Python 3.5.2. Please bear this in mind when 
installing dependencies etc.  

All of the project requirements are contained within `requirement.txt`
and assumes that you are familiar with using `virtualenv` and `pip`

To install the requirements for this project, run the following script
from the project root:
```
pip install -r requirements.txt
```

Once you have the requirements installed you should have Django 
installed and will need to run the following two steps to get going:
```
python manage.py migrate
python manage.py runserver 8000 (runs local server on port 8000)
```

### Installation notes
The above commands create a `sqlite` database called `db.sqlite3`. To
override this, and tweak other settings if you know what you're doing
rename `local_settings.py.sample` in the `settings` directory to 
`local_settings.py`.  You may need to delete any existing databases
and re-run the `migrate` command above to get these bespoke settings
working.
