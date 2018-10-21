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
* Python 3.6
* postman
* pip
* virtualenv

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

# Users
Users include staff(superusers) and Normal Users
# Staff (superuser)
#### Are created using the command
$ python manage.py createsuperusers
#### Functions the supers users can do
| Funcion                                 | Request| command                 |
| ------------------------------------------ | -------| ------------------------|
| `/api-token-auth/`                         |`POST`  | Login and retrieve token|
| `/api/account/`                            |`POST`  | Get User Account        |
| `/api/account/<user_id>/update/`           |`PUT`   | UPDATE User Account     |
| `/api/flight/create/`                      |`POST`  | Create Flight           |
| `/api/flight/`                             |`GET`   | GET All flights         |
| `/api/flight/<flight_id>/`                 |`GET`   | GET Flight Detail       |
| `/api/flight/<flight_id>/update`           |`PUT`   | Update Booking Details  |
| `/api/flight/<flight_id>/delete`           |`DELETE`| DELETE booking          |
| `/api/seat/create/`                        |`POST`  | Create Seat           |
| `/api/seat/`                               |`GET`   | GET All Seats         |
| `/api/seat/<seat_id>/`                     |`GET`   | GET Seat Detail       |
| `/api/seat/<seat/update`                   |`PUT`   | Update Booking Details  |
| `/api/seat/<seat/delete`                   |`DELETE`| DELETE booking          |
| `/api/bookings/customer/`                  |`GET`   | GET User bookings       |
| `/api/bookings/customer/create/`           |`POST`  | Create Booking          |
| `/api/bookings/<booking_id>/`              |`GET`   | GET booking Details     |
| `/api/bookings/<booking_id>/update`        |`PUT`   | Update Booking Details  |
| `/api/bookings/<booking_id>/`              |`DELETE`| DELETE booking          |
| `/api/payments/`                           |`GET`   | GET All payments        |
| `/api/payment/customer/`                   |`GET`   | Get customet payment    |
| `/api/payment/<booking_id>/`               |`GET`   | GET payment Details     |

# Normal Users (Normal Users)
#### Are through:
* the api /api/rest-auth/registration/
* sign up on the web app
#### Functions the normal user can do
| Funcion                                 | Request| command                 |
| ------------------------------------------ | -------| ------------------------|
| `/api/rest-auth/registration/`             |`POST`  | Register a new user     |
| `/api-token-auth/`                         |`POST`  | Login and retrieve token|
| `/api/account/`                            |`POST`  | Get User Account        |
| `/api/account/<user_id>/update/`           |`PUT`   | UPDATE User Account     |
| `/api/flight/`                             |`GET`   | GET APp flights         |
| `/api/flight/<flight_id>/`                 |`GET`   | GET Flight Detail       |
| `/api/flight/<flight_id>/update`           |`PUT`   | Update Booking Details  |
| `/api/flight/<flight_id>/delete`           |`DELETE`| DELETE booking          |
| `/api/bookings/customer/`                  |`GET`   | GET User bookings       |
| `/api/bookings/customer/create/`           |`POST`  | Create Booking          |
| `/api/bookings/<booking_id>/`              |`GET`   | GET booking Details     |
| `/api/bookings/<booking_id>/update`        |`PUT`   | Update Booking Details  |
| `/api/payment/customer/`                   |`GET`   | Get customet payment    |

# Running the tests
 $ python manage.py test
