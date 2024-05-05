from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(database_uri="sqlite:///ecommerce.db"):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config

    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    from .routes import main
    app.register_blueprint(main)
    return app
