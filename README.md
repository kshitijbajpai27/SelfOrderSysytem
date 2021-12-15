# Self Ordering System
Self ordering systems are fast becoming popular in restaurants.Customers can browse the entire menu at their own pace, an option preferred by many customers, rather than being hurried by a cashier.

## Installation

IDE used: VScode
Python and Django need to be installed

```bash
pip install django
```

```bash
pip install django-crispy-forms
```

```bash
pip install django-allauth
```

```bash
pip install Pillow==5.0.0
```

## Usage

Go to the Self order food folder -> deliver folder -> select manage.py -> run manage.py file

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Home page

The home page is open to all.It includes four basic tabs:

1-Deliver
2-About Us
3-Menu
4-Place an order
  
The username is 'admin' and password is 'jeetu123'. 
 
You can access the django admin page at **http://127.0.0.1:8000/admin** and login with username 'admin' and the above password.

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

Customers can access the services through homepage.
Admin can be added through the admin page. 

admin can access the admin page that is used to modify all dishes related informations such as item_name, item_id, item_price etc.

**For more details regarding the system and features please refer the reports included.**

## Update

Added method to reset order time range in Django Admin page.

This is present in Django Admin -> order (http://127.0.0.1:8000/admin/info/).  


This will showcase all present data and create new objects for the given time range. 


## Paypal Test id Password

paypal id = sb-tfpec6599205@personal.example.com
pass = (%EU!Hr9

Email ID: sb-pkuaw6599130@personal.example.com
System Generated Password: +$]kv@A8

Generated Credit Card Details

Card Type: Visa

Card Number: 4863379335561029

Expiration Date: 01/2022

CVV: 461

## Screenshots

![alt text](https://shorturl.at/ksS03)

![alt text](https://shorturl.at/ioBF9)

![alt text](https://shorturl.at/ablFS)

![alt text](https://shorturl.at/czIJM)

![alt text](https://shorturl.at/myJP4)

![alt text](https://shorturl.at/htAD8)

![alt text](https://shorturl.at/agmLX)

![alt text](https://shorturl.at/cnoEV)

![alt text](https://shorturl.at/kFL69)

![alt text](https://shorturl.at/stzL6)

![alt text](https://shorturl.at/jzAI9)

![alt text](https://shorturl.at/qACKQ)