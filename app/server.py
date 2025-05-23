from flask import Flask
from flask_jwt_extended import JWTManager
from .config import DB_URL, SECRET_KEY, JWT_EXPIRATION_DELTA
from .models import db
from .auth import auth_bp
from .resources import recursos_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_EXPIRATION_DELTA

    db.init_app(app)
    JWTManager(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp)
    app.register_blueprint(recursos_bp)
    return app
