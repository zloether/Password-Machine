# password-machine
Flask application that generates random passwords

See it live here: [https://passwordmachine.pythonanywhere.com/](https://passwordmachine.pythonanywhere.com/)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites
You'll need to have Python installed in order to run `password-machine`. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: `password-machine` has not been tested with Python 2 and may not work without changing some things.*

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
python password-machine/pm.py
```

This will start a Python webserver running on your local machine. Access the application at [http://localhost:5000](http://localhost:5000)