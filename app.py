#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>Cookies and Sessions Demo</h1>'

def expiration_time(delay):
    expiration_time=datetime.datetime.now()+datetime.timedelta(days=delay)
    return expiration_time

@app.route('/cookies', methods=["Get"] ) 
def cookies():
    # import ipdb; ipdb.set_trace()
    response=make_response({"message": "Hit cookies route!"}, 200)
    print("print",response) 
    print("request",request) 
    response.set_cookie("hello","hgdjd")
    response.set_cookie("farnoosh","Attar", expires=expiration_time(90), httponly=True)
    print("cookies",request.cookies) 
    return response

# DELIVERABLES
    # 1. Create a GET '/cookies' custom route
    # 2. In route function:
        # - set_trace and inspect request cookies
        # - set a cookie for hello=world
        # - set another for foo=bar
        # - set another for current_user=codetombomb
        # - on last cookie, set path, expiration date, max age, httpOnly    '
        # - use set_trace to access specific cookies on the request cookie object
    # 3. In the client:
        # - Use useEffect to send a GET request to '/cookies'
        # - parse resp as json and console.log resp
        # - console.log document.cookie
        # - Note the cookies that are marked as HTTP only 
    # 4. Use session to create encrypted current user_id
        # - generate app.secret_key -> Cheatsheet: https://furry-shrimp-4f0.notion.site/Cookies-and-Sessions-Cheatsheet-2e4cbcd1c8ee4d71b8b0da395ebb3fe4?pvs=4
        # - create a session and store a user_id=1
        # - inspect session cookie in the browser
        # - delete cookie on the browser and check request.cookies on the server side

if __name__ == '__main__':
    app.run(port=5555, debug=True)