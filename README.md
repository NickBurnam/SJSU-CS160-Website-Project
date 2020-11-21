Credit: Onthir (YouTube Tutorial)

Step 1: Install Heroku Toolbelt.

First, go to heroku.com and create a free account, the download heroku cli from its website based on your operating system. Then, open command Prompt in the root directory of your project file. The type the following command:

heroku login

 This will prompt you to input your credentials to login to heroku. Provide your account details and move to the next step.

Step 2: Make your Project Heroku Friendly.

You can't just simply upload your website to heroku and it will display the contents. You have to make your project heroku friendly by adding the following files to the root directory of your project.


Procfile

Procfile declares what type of application are you deploying. Type in the following line in the Procfile and save it.

web: gunicorn --pythonpath projectName projectName.wsgi --log-file -


requirements.txt

Requirements contains the libraries required for your project to be installed on live server, for example BeautifulSoup, and other libraries.requirements.txt looks something like this,

Django==2.0
dj-database-url==0.5.0
dj-static==0.0.6
gunicorn==19.9.0
Pillow==3.3.0
psycopg2-binary==2.7.7
whitenoise==4.1.2
django_ckeditor
django-crispy-forms

The above mentioned are the must have libraries and rest you can add by formatting in the same way.

runtime.txt

Runtime tells what version of python you are going to use. Type in the following way based on which version you're using.


python-3.7.0

Step 3: Setup static files for live server

In the settings.py file, at the end, add the following lines of code to serve your static files in a live server.


# POSTGRES DATABASE FOR PRODUCITON
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

Install the whitenoise

pip install whitenoise

Then, add whitenoise to your wsgi.py file


"""
WSGI config for nsaOfficial project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""


import os



from django.core.wsgi import get_wsgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nsaOfficial.settings')



application = get_wsgi_application()

Step 4: Deployment

Inorder to deploy your django app to heroku, you need to have a github or bitbucket account. After getting an account, create a repository and name it whatever you want. Then install git on your OS. Its pretty simple, simply search download git and install it. Then go to you project root and open command prompt or terminal or bash console or git console. Then type in the following commands.


git init
git remote add <your repo link>
E.g: git remote add https://github.com/markm-99/


git add .
git commit -m "Initial commit"
git push origin main -f 

Then, it will ask you to put in your credentials for github, provide the information and your project is now saved in that repo.

Now Type following commands:

heroku create <appname>
E.g: heroku create reviews99    (then your website url will be reviews99.herokuapp.com)
git push heroku main

If it shows, that the deployment was successful, you are almost done. If not, please follow the steps more carefully. Since, you can't use sqlite database in heroku, your all database will be empty and it will create a postgres database. Then type the following commands to migrate your database.

heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
Finally, heroku open, it will open your website. Then your website is now live.
