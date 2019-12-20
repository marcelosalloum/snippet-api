from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# Initialize dependencies
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config_class=Config):
    # Configure app
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    # models Blueprint
    from app.models import bp as models_bp
    app.register_blueprint(models_bp)

    # api Blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Link dependencies
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    return app
