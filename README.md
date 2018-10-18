# flight-booking-system


## Description

This is a django application for managing flight booking by automating the processes. The flight booking system provides an API that enables the user to:
* log in
* upload passport photographs
* book tickets
* receive tickets as an email
* check the status of their flight
* make flight reservations
* purchase tickets

The flight booking system should be able to:
* encrypt password
* handle multiple requests
* optimize via caching and multithreading

## Requirements

Python 3.6
postgresql9.6
postman
pip
virtualenv

# Installation
### 1)Clone the repo from GitHub:
$ git clone https://github.com/Ahmedsebit/flight-booking-system.git

### 2) Create a virtual environment and install the necessary packages with:
$ virtualenv -p python3 env

### 3) Activate virtual environment:
$ source env/bin/activate

### 4) cd to the root of the api:
$ cd flight-booking-system

### 5) Install requirements:
$ pip install -r requirements.txt

### 6) Make migrations:
$ python manage.py makemigrations

$ python manage.py migrate

### 8)Create Super User

$ python manage.py createsuperuser

# Runserver
$ python manage.py runserver

# Endpoints
| Endpoints                                  | Request| command                 |
| ------------------------------------------ | -------| ------------------------|
| `/api/rest-auth/registration/`             |`POST`  | Register a new user     |
| `/api-token-auth/`                         |`POST`  | Login and retrieve token|
| `/api/account/`                            |`POST`  | Get User Account        |
| `/api/account/<user_id>/update/`           |`PUT`   | UPDATE User Account     |
| `/api/flight/create/`                      |`POST`  | Create Flight           |
| `/api/flight/`                             |`GET`   | GET APp flights         |
| `/api/flight/<flight_id>/`                 |`GET`   | GET Flight Detail       |
| `/api/flight/<flight_id>/update`           |`PUT`   | Update Booking Details  |
| `/api/flight/<flight_id>/delete`           |`DELETE`| DELETE booking          |


# Running the tests
 $ python manage.py test
