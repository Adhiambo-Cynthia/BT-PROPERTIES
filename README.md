# DJANGO BT PROPERTIES PROJECT
This project aims in helping real estate companies and their clients in showcasing, buying and managing properties online.You can create a user account and send inquiries to the various realtors concerning a property of interest and they'll be automatically notified via an email.
### Technologies Used
* Python 3.7
* Bootstrap 4
* Django 3.0.7
* psycopg2 2.8.5
* psycopg2-binary 2.8.5z
* Pillow 7.2.0
* Postgresql

### Design Specs
* Mobile Friendly
* Social media icons & contact info
* Branded

### Functionality Specs
#### App User
* A display of realtors on about page with “seller of the month” 
* A display of listings in app with pagination
* Search listings by keyword, city, state, bedrooms and price (Homepage & search page)
*	Specific Listing page with images viewed through lightbox
* Register and login for their user accounts
* Listing page has a form to submit inquiry for that property listing
* User can track their inquiries on their dashboard
*	Form info should go to database and notify realtor(s) with an email
*	Frontend register/login to track inquiries
*	Both unregistered and registered users can submit form. If registered, can only submit one per listing

#### Admin
* Manage listings, realtors, contact inquiries and website users 
* Role based users (staff and non-staff)
* Ability to set listings to unpublished
* Choose 'seller of the month'




### Project Setup
1. On your file system, create a project folder for this named Real Estate_Django or any name of preference and open its command prompt.
2. create a virtual environment named **env** with the command 
```
python -m venv env
```
Using a virtual environment avoids installing Django into a global Python environment and gives you exact control over the libraries used in an application both in development and production mode.
You can activate your ```env``` by running ```env\Scripts\activate```

3. Depending on the code interpreter that you are using, select a python code interpreter that contains ```./env``` to it.
If you are using VS Code you can find guidance on how to go about this at [VS Code Django Setup Documentation](https://code.visualstudio.com/docs/python/tutorial-django)

4. You can then open the command terminal again containing the env and run the command
```
pip install django
```
### Create the Django Project
A "Django project" can be composed of one or more "apps" that you deploy to a web host to create a full web application.
To create a minimal Django app, then, it's necessary to first create the Django project to serve as the container for the app, then create the app itself.You can do this by running
```
django-admin startproject project_name .
```
* ```startproject``` command assumes (by use of ```.``` at the end) that the current folder is your project folder.
This then creates the project's Django command-line administrative utility ```manage.py``` and a sub-folder ```web_project_name``` that you chose.
* Then start Django's development server to make sure your virtual environment is set using the command ```python manage.py runserver``` . The server runs on the default port 8000. 

:rocket: you are now set to go! :tada:

### Installing the various packages
* We'll also be using psycopg2 as our PostgreSQL database adapter.This will enable us to be able to write SQL statements directly on our apps. To install:
```
pip install psycopg2
```
```
pip install psycopg2-binary
```
* After we make our models, we'll run ```python manage.py makemigrations``` to make migrations for the tables and apply them using ```python manage.py migrate``` which will create the tables inside our database.

* For the image fields in the models, we'll need to ```pip install Pillow```

### Customizing the admin app template stucture
The default templates used by the Django admin are located under the ``` /django/contrib/admin/templates/``` directory of your Django installation inside your operating system's or virtual env Python environment ```virtual_env_directory/lib/python3.5/site-packages/django/contrib/admin/templates/```.

All the Django admin templates inherit their behavior from the ```admin/base_site.html``` template, which itself inherits its behavior from the ```admin/base.html``` template.

### Additional Structures
1. In both forms for **'user registration'** and **'user login'**, we have utilized a CRSF Token
 ```python
 {% csfr_token %}
 ```
meant to prevent a CSFR attack.Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform.For example, this might be to change the email address on their account or to change their password unintentionally.

* The token basically ensures the requests made are:
  * Unpredictable with high entropy, as for session tokens in general.
  * Tied to the user's session.
  * Strictly validated in every case before the relevant action is executed.

