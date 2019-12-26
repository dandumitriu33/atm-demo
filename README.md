# ATM - demo

Educational project. Simulation of an ATM machine progam.

quick look - https://flaskatmdemo.herokuapp.com/

## Technologies used:
- Flask - Python framework for web apps http://flask.palletsprojects.com/en/1.1.x/
- HTML and CSS
- database - SQLAlchemy https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- deployed on heroku.com https://www.heroku.com/

## Local installation (Ubuntu 18.4+)
- clone/download the project inside a parent directory
- on Ubuntu Python 3 should be installed by default, if not
please install it - https://www.python.org/
- install pip - https://pip.pypa.io/en/stable/

        sudo apt-get install python3-pip

- install virtualenv - https://virtualenv.pypa.io/en/latest/

        sudo pip3 install virtualenv
        
- create the virtual environment and activate it inside the project directory

        virtualenv venv
        source venv/bin/activate
        
- now switch to the app directory, the one cloned, not the main directory and install the 
contents of requirements.txt

        pip3 install -r requirements.txt
        
- run the server in the project app directory with 

        python3 server.py
        
## How to use  
Pretty intuitive UI, try to think of it as an actual ATM, pretend you only have the number keys and a 
touchscreen.

On the top right on the first page there's the card simulator :)

