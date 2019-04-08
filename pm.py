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
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
return "Hello World!"

if __name__ == "__main__":
app.run()