# PizzaPalace

PizzaPalace is a website for online pizza shopping made with a Django wireframe and has a postgreSQL database.
This readme file will tell you how to start the project, as well as some basic information about the program.
The project was originally designed in 2560x1440px resolution and is best experienced with said resolution.

## Installation

To start using the project, you will need to pip install two packages.
In the terminal you will need to type:
    
    pip install django
    pip install psycopg2-binary

After that, you should have everything you need.

## Activating site

To begin with, you'll need to navigate inside the right files.
Inside the parent folder type...

    cd .\PizzaPalace\PizzaPalace\

To activate the site then type inside the terminal:

    py manage.py runserver

This should activate the server on port: http://127.0.0.1:8000/
You can now connect to the site using your browser.

## Basic information

The site is made up of multiple subfolders inside the second PizzaPalace folder.
These are: cart, confirmation, homepage, main, menu, offer, pizza and user.

Here below is a basic description of all folders and their purpose:
    - main: This is the main folder of the Django wireframe. This mostly holds the base settings and other django basics.
    - pizza: This is the main app folder for the Django wireframe. Inside you will find all the html templates, the javascript and css file, all images and most of our models. This is basically a storage for all others views and apps.
    - cart: This is the app for all cart related things. All code for manipulating the cart cookie and displaying the right information sites for checkout are found here.
    - confirmation: This is the app for the confirmation page. Not much else.
    - homepage: This is the app that starts the homepage.
    - menu: This is the app that handles all things related to the menu page and the closer inspection of pizzas.
    - offer: This is the app that handles all things related to the offer page and the closer inspection of offers.
    - user: This is the app that handles all logins and sign ups and everything related to customer profiles.

## Rules 

In a previous design report we had stated we would use snake_case when naming our python functions as well as javascript functions, however this has changed. All python functions have instead been changed to all lowercaps, whilst javascript functions have become CamelCase.
Aditionally there are only singular empty newlines between python functions, instead of two.

The reason for these changes are quite simple. We believed ourselves to be using classes much more frequently than functions, and therefore believed we needed a way to indicate between them. But as the Django wireframe is usually more function heavy (at least in our instance) we ended up simply switching to all lowercase for ease of typing.

## Notes for grading

If you wish to see an example of a product with a long description please select the Margharita in the menu.

## Creators

This project was developed By Ágúst Máni Þorsteinsson, Hermann Helgi Þrastarsson og Aleksander Milenkoski.