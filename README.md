# password-machine
[![Python](https://img.shields.io/badge/python-v3.4+-blue.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/zloether/password-machine.svg?branch=master)](https://travis-ci.org/zloether/password-machine)
[![Issues](https://img.shields.io/github/issues/zloether/password-machine.svg)](https://github.com/zloether/password-machine/issues)
[![License](https://img.shields.io/github/license/zloether/password-machine.svg)](https://opensource.org/licenses/MIT)

Flask application that generates random passwords

See it live here: [https://passwordmachine.pythonanywhere.com/](https://passwordmachine.pythonanywhere.com/)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites
You'll need to have Python installed in order to run `password-machine`. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: `password-machine` has been tested with Python 2.7, however Python 3.4 or greater is recommended.*

## Installation
Download the latest version from GitHub using Git:
```
git clone https://github.com/zloether/password-machine.git
```
This will create a directory called *password-machine* and all the code will be in it.

Switch to the *password-machine* directory:
```
cd password-machine
```

Install the required packages:
```
pip install -r requirements.txt
```

## Usage
Launch the application:
```
python password_machine/pm.py
```

This will start a Python webserver running on your local machine. Access the application at [http://localhost:5000](http://localhost:5000)