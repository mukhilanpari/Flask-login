## Requirements.txt
    Flask
    Flask-SQLAlchemy

## Setup
```
python3 -m venv venv
venv\Scripts\activate
pip install flask
pip install Flask-SQLAlchemy
python app.py
```

## To view Database
```
1. login is implemented
2. Register the user
3. Updating the profile

To View,

sqlite3 test.db
.tables
select * from user;
select * from profile;
``` 
