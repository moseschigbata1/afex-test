# afex-test
A Django app test for Afex commodity exchange 

-------------------
**Atleast Python 3.6 is required**

**Technology Used:** Django 2.0.6 (Python 3)

**Database:** SQLite 3 (SQLite is used because it can be safely assumed that it would not be a very busy site and enterprise level database can be avoided)



## Installation

- Clone repository

    ```bash
    git clone https://github.com/Akoh1/afex-test.git
    ```

- Setup virtualenvironment with virtualenvwrapper

    ```bash
    mkvirtualenv name_of_virtualenv
    ```

- Install requirements

    ```bash
    pip install -r requirements.txt
    ```
- Migrate
     ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
## To view tasks in api
runserver and visit path 127.0.0.1:8000/api/v1/. 

    
## To Token authentication
 - create super user
    run python manage.py createsuper
 - use super user credentials to log in
    runserver and visit path 127.0.0.1:8000/api/v1/rest-auth/login/. 
