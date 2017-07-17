[![Build Status](https://travis-ci.org/andela-angene/py_dms.svg?branch=develop)](https://travis-ci.org/andela-angene/py_dms)

# PyDMS - Fullstack Document Management System

## How to Install
1. Clone the repo and cd into the folder
2. create a virtual env and activate it: `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt` (on mac, if you need to install postgres, run `brew install postgresgl`)
4. migrate the sqlite database: `python manage.py makemigrations && python manage.py migrate`
5. Start the app: `python manage.py runserver`
