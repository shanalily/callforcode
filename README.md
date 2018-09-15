# Call for Code project

## Developer Instructions

Install requirements:
```
pip install -r requirements.txt
```
Install and set up Postgres https://www.postgresql.org/download/. Create a database for
```
CREATE DATABASE callforcode;
```
Set environment variable for database URL.
```
export SQLALCHEMY_DATABASE_URI = *your database uri*
```

To run the application:
```
python run.py
```
