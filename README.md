# archiveorgconcertdownloader
Hate having to search through tons of unnecessary bands just to get a few concerts from Archive.org on your device? Me too! Enter: this Python based project that allows the user to quickly grab full concert rips of given bands. Made with 'The Internet Archive Python Library' (https://archive.org/developers/internetarchive/), and 'Django' (https://www.djangoproject.com/).

## Initial Setup
Activate the 'venv' instance by using the following command:
`source .venv/bin/activate`

Now that you have activated the 'venv' virtual environment, you will need to install the dependencies for this project via this command:
`pip3 install -r requirements.txt`

You will then need to tie your Internet Archive account to your project as well as I don't distribute my own. This is to cut down on abuse of bandwidth on a specific account, and this project is meant to be just run for personal use:
`ia configure`

You will need to create an admin account using this command:
`python manage.py createsuperuser`

You will then need to visit the following page in order to create a new 'Band' database entry that was created from the 'Band' model. This is so that you can select a new option from the initial dropdown to search for that particular band:
- http://127.0.0.1:8000/admin/concertdownloader/band/

## Screenshots:
<img width="1440" alt="Screenshot 1" src="https://github.com/user-attachments/assets/9bac9699-5d5d-4d02-bf01-657aa3b9064f" />

<img width="1440" alt="Screenshot 2" src="https://github.com/user-attachments/assets/8aceb5b5-c17e-4462-8516-c7aa87998798" />

<img width="1440" alt="Screenshot 3" src="https://github.com/user-attachments/assets/f159fb2a-f963-4ba6-a075-ad5f322aeaaf" />

<img width="323" alt="Screenshot 4" src="https://github.com/user-attachments/assets/29acc5a6-e0fb-481f-9fc3-3ac4e13cb9ae" />

## Mirrors
This project is also mirrored to BitBucket so that I can also play around with BitBucket Pipelines via CI/CD pipeline scripts:
- https://bitbucket.org/sambanya/archiveorgconcertdownloader/src/main/


