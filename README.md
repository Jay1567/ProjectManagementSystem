# _Project Management System_

---
### _Downloads_

Download [Python](https://www.python.org/downloads/release/python-397/)  [Preferably Python 3.8]

Download [Node.js](https://nodejs.org/en/)

---
### _Initial Setup_ 
```bash
mkdir ProjectManagementSystem 
cd ProjectManagementSystem/

#Clone Repo
git clone https://github.com/Jay1567/ProjectManagementSystem.git

#Create a virtual environment 
virtualenv env

#Activate virtual environment
#[For MacOS or Linux]
source env/bin/activate
#For[Windows]
env\Scripts\activate

##If virtualenv is not available run:
pip install virtualenv

#Install python packages
pip install -r requirements.txt 

#Navigate to frontend folder and install npm library:
cd ProjectManagementSystem-Project/frontend && npm install

#Make Database Tables:
cd ..
python manage.py makemigrations
python manage.py migrate
```

---
### _Run Project_ 

```bash
#To Compile React app:

#Navigate to frontend folder:
cd ProjectManagementSystem-Project/frontend

#To build for development:
npm run dev
#To build for production:
npm run build


#To run Django server [from base directory]:
cd ProjectManagementSystem-Project/
python manage.py runserver
```

[React App: localhost:8000/](localhost:8000/)

[Django Admin Panel: localhost:8000/admin](localhost:8000/admin)

[View APIs: localhost:8000/api/v1/](localhost:8000/api/v1/)

Create .env file locally to save credentials 
```shell
cd ProjectManagementSystem-Project
touch .env 
```

.env file:
```shell
SECRET_KEY=django-insecure-ij7kpqt^9xw679mgn^&x(ev)l)i+een6)gy$p5p8zpbozb+$4-
DEBUG=True
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB_NAME=<DATABASE_NAME>
POSTGRES_USER=<POSTGRES_USER>
POSTGRES_PWD=<POSTGRES_PASSWORD>
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=
EMAIL_PORT=465
EMAIL_USE_TLS=True
```