from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(testing=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLACHEMY_ECHO'] = True

    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else: 
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
    
    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['TESTING']= True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
    
    db.init_app(app)
    migrate.init_app(app,db)
    from .routes import planet_bp
    app.register_blueprint(planet_bp)
    from app.models.planet import Planet
    return app
