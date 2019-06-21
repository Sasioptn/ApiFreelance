# FreelanceApi


This Api server for freelance exchange.

## Install and run
> Clone project

```
git clone https://github.com/Sasioptn/ApiFreelance.git`
cd ApiFreelance 
```


- install virtual environment for project
```
$ sudo apt install virtualenv
$ virtualenv --python=python3.7 venv
```
- activate venv
```
$ source venv/bin/activate
```

> install all packages
```
$ pip install -r requirements.txt
```
> configure project settings
```
$ cd  api_freelance
$ touch secrets.py
```
> write in secrets.py your own secret key like this
```
SECRET_KEY = 'your own secret key'
```


> finally run project

```
$ python manage.py runserver
```
