# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

import click
from flask import Flask, render_template
from flask_wtf.csrf import CSRFError

from .blueprints.admin import admin_bp
from .blueprints.auth import auth_bp
from .blueprints.chat import chat_bp
#from .blueprints.oauth import oauth_bp
from .extensions import db, login_manager, csrf, socketio, moment#, oauth
from .models import User
from .settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'production')

    app = Flask('catchat')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_errors(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    socketio.init_app(app)
    moment.init_app(app)
    #oauth.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    #app.register_blueprint(oauth_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(admin_bp)


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('error.html', description=e.description, code=e.code), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', description=e.description, code=e.code), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error.html', description='Internal Server Error', code='500'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('error.html', description=e.description, code=e.code), 400


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--nn', default="", help='nickname')
    @click.option('--email', default="", help='email')
    @click.option('--pawo', default="", help='password')
    def forge(nn, email, pawo):
        """Generate fake data."""
        click.echo('Initializing the database...')
        db.drop_all()
        db.create_all()

        click.echo('Forging the data...')
        admin = User(nickname=nn, email=email)
        admin.set_password(pawo)
        app.config['CATCHAT_ADMIN_EMAIL'] = email
        db.session.add(admin)
        db.session.commit()

        click.echo('Done.')
