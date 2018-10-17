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

1)Clone the repo from GitHub:

git clone https://github.com/Ahmedsebit/flight-booking-system.git

1) Create a virtual environment and install the necessary packages with:

2) cd to the root of the api -- cd flight-booking-system

3) Activate the virtualenvironment -- source env.bin.activate

4)Intall the requirements pip install -r requirements.txt

# Initialize the a database

Make migrations
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade

# Create Super User

$ python manage.py createsuperuser

# Runserver and add the endpoints to postman

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
| `/api/seats/create/`                        |`POST`  | Create Flight           |
| `/api/seats/`                               |`GET`   | GET APp flights         |
| `/api/seats/<seat/update`                   |`PUT`   | Update Booking Details  |
| `/api/seats/<seat/delete`                   |`DELETE`| DELETE booking          |
| `/api/bookings/customer/`                  |`GET`   | GET User bookings       |
| `/api/bookings/create`                     |`POST`  | Create Booking          |
| `/api/bookings/<booking_id>/`              |`GET`   | GET booking Details     |
| `/api/bookings/<booking_id>/update`        |`PUT`   | Update Booking Details  |
| `/api/bookings/<booking_id>/delete`        |`DELETE`| DELETE booking          |
| `/api/payments/`                           |`GET`   | GET All payments        |
| `/api/payment/customer/`                   |`GET`   | Get customet payment    |
| `/api/payment/<booking_id>/`               |`GET`   | GET payment Details     |
| `/api/payment/create`                      |`POST`  | Create Payment          |

# Running the tests

 $ python manage.py test
