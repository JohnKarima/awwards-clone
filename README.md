# Project Name 
Awwards

# Project Description 
-  An application like that will allow a user to post a project he/she has created and get it reviewed by his/her peers.

# Link to Live Project
- https://awwardsclone343.herokuapp.com

# Access the APIs
- https://awwardsclone343.herokuapp.com/api/project
- https://awwardsclone343.herokuapp.com/api/profile

# Author 
- [John Karima](https://github.com/JohnKarima)

# Setup Instructions 

### Cloning
```
$ git clone https://github.com/JohnKarima/awwards
```
### Move into directory and install requirements
```
$ cd awwards

$ pip install -r requirements.txt 
```
### Install and activate a Virtual Environment
```
$ python3 -m venv virtual 

$ source virtual/bin/activate  
```
### Set-up a Database
```
Set your database User and Password 
```
### Make Migrations & Migrate
```
$ python manage.py makemigrations <DB Name> 

$ python manage.py migrate 
```
### Run the application
```
python manage.py runserver 
```
### Run the test for the application
```
$ python3 manage.py test awwards
```

# Technologies Used
- Python
- Django
- Bootstrap
- pillow
- cloudinary
- crispy forms
- djangorestframework

# Contact Information
karimajohn24@gmail.com

# License Copyright 
- 2020, John Karima.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

