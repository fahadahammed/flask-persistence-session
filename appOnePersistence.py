# Created By Fahad Ahammed
# www.fahadahammed.com
# Github: fahadahammed
# 2018-11-10_18-26


from flask import Flask, session
from flask_session import Session

import datetime

import redis

app = Flask(__name__)

# Session
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.from_url('127.0.0.1:6379', db=0 )
app.config['SESSION_COOKIE_SECURE'] = True

Session(app)


@app.route('/')
def hello_world():
    timeNow = datetime.datetime.now()

    if "application_name" not in session:
        application_name = "appOne" + str(timeNow.strftime("%Y-%m-%d_%H-%M-%S"))
        session['application_name'] = application_name + "/n Session"

    if "application_name" in session:
        return session['application_name']
    else:
        application_name = "appOne" + str(timeNow.strftime("%Y-%m-%d_%H-%M-%S"))
        return application_name


if __name__ == '__main__':
    app.secret_key = "appOneSecretKey"
    app.env = "Development"
    app.debug = True
    app.run(host="127.0.0.1", port="6001")