from flask import Flask
# to import flask

app = Flask(__name__)
# creating an app variable to be used throughout flask application

from app import routes
# routes have to be imported after app variable created, otherwise will break
