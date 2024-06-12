from flask import Flask

from .error_handler import error_not_found
from app.config import config
from app.routes.movie import movie_bp


app = Flask(__name__)


def create_app():
    # Config
    app.config.from_object(config["development"])

    # Blueprints
    app.register_blueprint(movie_bp, url_prefix='/api/movie')
    
    # Handle errors
    app.register_error_handler(404, error_not_found)

    return app