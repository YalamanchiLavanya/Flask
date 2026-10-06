#pip install flask

import flask
from flask import Flask

#we will initialize the Flask application instance
app = Flask(__name__)

#now we will define a route for the URL
@app.route('/')
def home():
    return "Day1 of Learning Flask"

if __name__=="__main__":
    #run the local development server
    app.run()
