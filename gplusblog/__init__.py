from flask import Flask
from flaskext.script import Manager


def create_app(config_filename='default_settings.py'):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_pyfile(config_filename)
    from urls import setup_urls
    setup_urls(app)
    return app


def create_manager(app):
    return Manager(app)


def main():
    import commands
    commands.run_manager()
