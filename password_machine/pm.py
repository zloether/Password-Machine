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
from flask import Flask, request, render_template, Markup, url_for
import markdown
import passgenerator
import os.path


# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------
app = Flask(__name__)
app_path = os.path.dirname(os.path.realpath(__file__))
templates_folder = os.path.join(app_path, 'templates')
index_md = os.path.join(templates_folder, 'index.md')



# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
@app.route("/")
def index():
    with open(index_md, 'r') as f:
        content = f.read()
    content = Markup(markdown.markdown(content, extensions=['markdown.extensions.tables']))
    return render_template('index.html', **locals())
    


@app.route("/random-password", methods=['GET', 'POST'])
def random_password():
    if request.method == 'GET':
        upper = request.args.get('upper', default = "", type = str)
        lower = request.args.get('lower', default = "", type = str)
        numbers = request.args.get('numbers', default = "", type = str)
        special = request.args.get('special', default = "", type = str)
        length = request.args.get('length', default = 32, type = int)

    elif request.method == 'POST':
        upper = request.form.get('upper')
        if not upper:
            upper = 'false'
        
        lower = request.form.get('lower')
        if not lower:
            lower = 'false'
        
        numbers = request.form.get('numbers')
        if not numbers:
            numbers = 'false'

        special = request.form.get('special')
        if not special:
            special = 'false'
        
        length = request.form.get('length')
        if length == None:
            length = 32
        else:
            length = int(length)

    else:
        print('Err: unsupported request method')

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