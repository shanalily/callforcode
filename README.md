# Call for Code project

Mallory Gaspard - gaspam3@rpi.edu
Shoshana Malfatto - malfas@rpi.edu
Joseph Souto - soutoj@rpi.edu

## Github Repo Link:
https://github.com/shanalily/callforcode 

## Project Description  
When diasaster strikes and help is desperately needed, one of the most signficant contributors to the chaos is misallocation and disorganization of volunteers and aid services. After seeing countless images on national news of disaster reilef volunteers being turned around due to miscommunications, hearing horror stories of people waiting for hours on their roofs during hurricanes for help to arrive, and even watching one of the creator's family get rescued from their flooded home via volunteer canoe since no emergency vehicles were availible at the time, the creators decided to develop the Optimal Relief Scheduler App, in order to optimize the process. Employing machine learning, image recognition technologies, and network analysis, we are able to determine the most efficient ways to allocate volunteers, while determining levels of risk due to disaster damage in order to ensure that volunteers arrive with the aid equipment most useful for saving victims and to ensure volunteer and victim safety as well. Thus, in short, ORSA - Optimal Relief Scheduler App is a web application that employs machine learning image recognition and network science to determine efficient allocation of volunteer resources and accurate risk assessment to ensure volunteer and victim safety.

## Requirements

* Python 3.5.2 and above
* Postgres 9.5.13 and above

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
Install and set up Postgres https://www.postgresql.org/download/. You can create a role and a password.
Create a database for project:
```
CREATE DATABASE callforcode;
```
Set environment variable for database URL.
```
export SQLALCHEMY_DATABASE_URI="postgres://<role>:<password>@localhost/<dbname>"
export CFC_SECRET_KEY=0 # this can be anything for now
```

To run the application:
```
python run.py
```
