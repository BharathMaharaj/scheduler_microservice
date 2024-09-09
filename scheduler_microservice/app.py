from flask import Flask
from config import Config
from routes import app as routes_app
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(routes_app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
