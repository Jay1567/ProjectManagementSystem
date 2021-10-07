# _Project Management System_

---
### _Downloads_

Download [Python](https://www.python.org/downloads/release/python-397/)  [Preferably Python 3.9]

Download [Node.js](https://nodejs.org/en/)

---
### _Initial Setup_ 
```bash
mkdir ProjectManagementSystem 
cd ProjectManagementSystem/

#Create a virtual enviornment 
virtualenv env

#Activate virtual enviornment
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
