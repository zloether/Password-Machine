#!/usr/bin/env python

#########################################################################################
# NAME: pm.py
# 
# Website: https://github.com/zloether/password-machine.git
#
# Description: Python Flask application that outputs a random password
#########################################################################################


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from flask import Flask, request
import passgenerator
app = Flask(__name__)



# -----------------------------------------------------------------------------
# methods
# -----------------------------------------------------------------------------
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/random-password")
def random_password():
    upper = request.args.get('upper', default = "", type = str)
    lower = request.args.get('lower', default = "", type = str)
    numbers = request.args.get('numbers', default = "", type = str)
    special = request.args.get('special', default = "", type = str)
    length = request.args.get('length', default = 32, type = int)

    if upper.lower() == 'false':
        upper = False
    else:
        upper = True
    
    if lower.lower() == 'false':
        lower = False
    else:
        lower = True
    
    if numbers.lower() == 'false':
        numbers = False
    else:
        numbers = True
    
    if special.lower() == 'false':
        special = False
    else:
        special = True

    password = passgenerator.generate(length=length, upper=upper, lower=lower, numbers=numbers, special=special)
    return password



# -----------------------------------------------------------------------------
# runner
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run()