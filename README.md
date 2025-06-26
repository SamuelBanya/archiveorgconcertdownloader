# archiveorgconcertdownloader
Hate having to search through tons of unnecessary bands just to get a few concerts from Archive.org on your device? Me too! Enter: this Python based project that allows the user to quickly grab full concert rips of given bands. Made with 'The Internet Archive Python Library' (https://archive.org/developers/internetarchive/), and 'Django' (https://www.djangoproject.com/).

## Initial Setup
Activate the 'venv' instance by using the following command:
`source .venv/bin/activate`

Now that you have activated the 'venv' virtual environment, you will need to install the dependencies for this project via this command:
`pip3 install -r requirements.txt`

You will then need to tie your Internet Archive account to your project as well as I don't distribute my own. This is to cut down on abuse of bandwidth on a specific account, and this project is meant to be just run for personal use:
ia configure

You will need to create an admin account using this command:
`python manage.py createsuperuser`

You will then need to visit the following page in order to create a new 'Band' database entry that was created from the 'Band' model. This is so that you can select a new option from the initial dropdown to search for that particular band:
- http://127.0.0.1:8000/admin/concertdownloader/band/