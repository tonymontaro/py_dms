[![Build Status](https://travis-ci.org/andela-angene/py_dms.svg?branch=develop)](https://travis-ci.org/andela-angene/py_dms)

# PyDMS - Fullstack Document Management System

PyDMS is an application that helps users manage their documents in an organized way. A User can create a document, edit and share it with others.
The application utilizes RESTFUL API architecture for managing documents, users and roles.

[Click here](https://montarojed-pydms.herokuapp.com) to view the app, hosted on Heroku.


## Features

The app has three levels of authorization;
- Guest can
    - view public documents on the website
    - create an account

- A regular user can:
    - create documents
    - edit and Delete his/her document
    - edit and Delete his/her profile
    - limit access to a document by specifying an access level to public, private or role.
    - view public documents created by other users.
    - login/logout.

- An admin user has all the previlages of a regular user and do the following too:
    - view all users.
    - update a user's role e.g upgrade another user to admin.
    - create roles.
    - edit and delete existing roles
    - Delete created roles aside form the admin role

## Technologies
The application was developed with [Django](https://www.djangoproject.com/), [Django REST framework](http://www.django-rest-framework.org/) was used for routing and [Postgres](http://postgresql.com/) was used for database management.
 [ReactJS](https://reactjs.org/) with the Redux architecture was used to build the client side of the application

## Installation
Follow the steps below to setup a local development environment. First ensure you have [Postgresql](https://www.postgresql.org/)  and Python installed.

## How to Install
1. Clone the repo and cd into the folder
2. create a virtual env and activate it: `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt` (on mac, if you need to install postgres, run `brew install postgresgl`)
4. Export the following environment variables used by the application(e.g `export DATABASE_HOST='localhost'`):
    - DATABASE_NAME
    - DATABASE_USER
    - DATABASE_PASSWORD
    - DATABASE_HOST

    refer to [this](https://stackoverflow.com/questions/9554087/setting-an-environment-variable-in-virtualenv) if you would like to load the variables automatically.

5. migrate the database: `python manage.py makemigrations && python manage.py migrate`
6. Start the app: `python manage.py runserver`


## Testing
Ensure that project dependencies are installed before running tests.
### Server tests
The server tests files are located in a *test* folder inside the *main* app

1. Open a terminal and navigate to the project directory
2. run `python manage.py test main/test`

## API Summary
View full API documentation [here](https://montarojed-pydms.herokuapp.com/api)

### Users
EndPoint                      |   Functionality
------------------------------|------------------------
POST /users/login         |   Logs in a user and returns a token.
POST /users/              |   Creates a new user.
GET /users/               |   Gets all users (available only to the Admin).
GET /users/:id           |   Find a user by id.
PUT /users/:id           |   Updates a user's profile based on the id specified (available to the profile owner or admin)
DELETE /users/:id        |   Delete a user's profile (available only to the profile owner)
GET /users/:id/documents   | Gets all documents for a particular user
GET search/users/?q=${query} | Get all users with username containing the search query

### Documents
EndPoint                      |   Functionality
------------------------------|------------------------
POST /documents/          |   Creates a new document instance.
GET /documents/           |   Gets all documents.
GET /documents/:id       |   Find document by id.
PUT /documents/:id       |   Updates a document's attributes. (available only to the author)
DELETE /documents/:id    |   Delete a document. (available only to the author)
GET search/documents/?q=${query} | Get all documents with title containing the search query

### Roles (available only to the Admin)
EndPoint                      |   Functionality
------------------------------|------------------------
GET /roles/               |   Get all Roles.
POST /roles/               |   Create a Role.
PUT /roles/:id               |   Edit a Role.
DELETE /roles/:id               |   Delete a Role.

### Contributing

Contributions are most welcome. Simply fork the repository, work on the feature and raise a PR.

### Licence
MIT
