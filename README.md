# DJANGO CAD PROPERTIES PROJECT
For complete beginners, I'm gonna help you with basic set up.
### Setting up the django project
1. On your file system, create a project folder for this named Real Estate_Django or any name of preference and open its command prompt.
2. create a virtual environment named **env** with the command 
```
python -m venv env
```
Using a virtual environment avoids installing Django into a global Python environment and gives you exact control over the libraries used in an application.

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