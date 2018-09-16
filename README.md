# Call for Code project

## Requiremetns
Python 3.5.2 and above
Postgres 9.5.13 and above

## Developer Instructions

Clone repository:
```
git clone git@github.com:shanalily/callforcode.git
cd callforcode
```
Install requirements:
```
pip install -r requirements.txt
```
Install and set up Postgres https://www.postgresql.org/download/. Create a database for project:
```
CREATE DATABASE callforcode;
```
Set environment variable for database URL.
```
export SQLALCHEMY_DATABASE_URI="postgres://<role>:<password>@localhost/<dbname>"
```

To run the application:
```
python run.py
```
