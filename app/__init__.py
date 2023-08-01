from flask import Flask
from flask_bcrypt import Bcrypt

from app.main.config import Config
from app.api.repository import db
flask_bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    flask_bcrypt.init_app(app)

    # Blueprints
    from app.main.routes import bp
    app.register_blueprint(bp)

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/test/')
    def test():
        return '<h1>Test Flask Route</h1>'

    return app
