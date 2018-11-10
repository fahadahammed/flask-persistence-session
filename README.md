# flask-persistent-session
This is an application showing how you can build Flask Applications with persistent session.


## Create Environment
```bash
$ virtualenv .virtualenvironment --python=python3
```

Activate it

```bash
$ source .virtualenvironment/bin/activate
```

## Full fill requirements

```bash
$ pip install -r requirements
```

You also need redis installed in your system.

## Description

This repository has a pseudo code to have persistent session data for flask application.
There are 4 pseudo flask application that returns application name and date-time.

Non-Persistent:

- appOne.py
- appTwo.py

If you run both of these, you will see different return value.

Persistent:

- appOnePersistence.py
- appTwoPersistence.py

If you run these two, You will see same output in both of the applications return.


## Tags
flask persistence, flask application session persist, microservice flask session


## Reference
- Flask-Session