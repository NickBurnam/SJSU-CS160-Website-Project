This is Team 1's site for CS160 Fall 2020, at SJSU.

Steps to view site locally:

1) Install a recent version of Python to your system
2) Either clone the repository, or extract any zip file contents to a new directory. (Note that the repository does not include a provided sqlite db file).
3) From a command line terminal, CD to this new directory.
4) Create a new virtual environment in this folder. The method will differ depending on your OS.
	For Windows, run: python -m menv env
	For OSX, run: pipenv shell
	  (and you may want to follow up with a rename of the new virtual environment folder)
5) (Optional Step) To enable email-notifications on the site, open up your new activate script file and add lines to set some environment variables that will be used for the site:
	For Windows, add the commands:
		set EMAIL_HOST_ADDRESS=smtp.sendgrid.net
		set EMAIL_HOST_PORT=587
		set EMAIL_HOST_USER=apikey
		set EMAIL_HOST_PASSWORD=<provided separately>
		set SENDGRID_API_KEY=<provided separately>
	For OSX, do the same commands but instead of "set", use "export"
6) Activate your new virtual environment via activate file
7) Install needed libraries into your virtual environment via: pip install -r requirements.txt
8) Start up the site via: python manage.py runserver
9) Visit the site by copying-pasting the address provided from the terminal (likely http://127.0.0.1:8000/ )


Admin account username: admin
password: team1isnumba1

The admin account is needed to add in new 'Course' entries via the admin section ( http://127.0.0.1:8000/admin/ )
Blog entries can be added from the site directly when logged in.