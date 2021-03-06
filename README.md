#  Awward

#### Author: [Clement Lumumba](https://github.com/Clemo97)


* Link to live site: [Awward](https://clemo-award.herokuapp.com/)

## Description
The application will allows a user to post a project he/she has created and get it reviewed by his/her peers.

## Home Page
![Alt text](static/1.png?raw=true "Title")
![Alt text](static/2.png?raw=true "Title")

As a user of the web application you will be able to:

1. Sign up and log in
2. View projects posted by other users
3. Post projects
4. Rate a project
5. Edit your profile
6. Generate APIs

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if already have an account |if you dont have , click on the sign up link and fill the form  | If login is successful, user is navigated to home page | Click on `Comment` | Taken to where you can comment | Signs In/ Signs Up |
| Edit profile | On the account link, click on the   profile to update| Redirected to the profile page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
|Add a new project|Click on the add project icon to be redirected to the new post form|the post will be rendered to the home page
| Click on log Out in the accounts| Redirects to the login form | Logs out user  |

## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/Clemo97/awwards.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'q#h0zgxq36zn1hm!w9xddz06k71vun(&#c((%dje09_-'4-n**9qrqjf%zmw!_npld)l'
DEBUG=True
DB_NAME='awwards'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test awward`
        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Django 2.2.8
* Postgresql 
* Boostrap
* HTML
* CSS


## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :lumumbaclement@gmail.com

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)