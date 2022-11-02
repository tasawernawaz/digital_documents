# Digital Documents Store
A test project to store digital documents in folders. For the time being I am assuming that there wont be any authentication.

### How to run

Once you have clonned this repo.

`git clone git@git.toptal.com:screening/TasaweTasawer.git`

#### Create virtual enviroment

`python3 -m venv /path/to/new/virtual/environment`

after creating, activate it. More details can be found at https://docs.python.org/3/library/venv.html


### Install Requirements

Run the following command from `/backend`

`pip install requirements.txt -r`

### Run server

`./manage.py runserver`

API docs should be availabe at http://127.0.0.1:8000/swagger/

### Run tests

- To run all tests use `pytest`
- To run specific test file use path to the class or test mehtod. e.g `pytest tests/test_api.py::DocumentViewSetTests::test_list_documents`

## Filtering on folders and Topics

Documents can be filtered based on folder name and topics (comma separated). e.g

    1. `?folder=english&topics=gaming,learning`
    2. `?folder=english`
    3. `?topics=gaming,learning`


## ERD

ERD available at `/docs` folder.
