# project/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'  # Change this to your PostgreSQL URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Import models and views at the end to avoid circular imports
from project import models

# Import views here after models and app are initialized
import project.views  # Use this syntax to avoid circular imports
