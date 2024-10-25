import os
from flask import Flask
import click
from .scrapercm import scrape
from .selectdb import select_all

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import view
    app.register_blueprint(view.bp)
    app.add_url_rule('/', endpoint='index')

    from . import scrapercm
    app.cli.add_command(scrape)

    from . import selectdb
    app.cli.add_command(select_all)

    return app
