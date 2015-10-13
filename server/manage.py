#! /usr/bin/env python
import os
from flask import jsonify
from flask.ext.script import Manager, Shell, Command, Server
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.security.datastore import SQLAlchemyUserDatastore
from flask.ext.security import Security, http_auth_required

from api import create_app, db
from api.models import User, Role
# from . import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


def make_shell_context():
    return dict(app=app, db=db)


class DBInit(Command):
    ''' Creates tables from SQLAlchemy models. '''

    def __init__(self, db):
        self.db = db

    def run(self):
        self.db.create_all()


class DBRegUser(Command):
    ''' Creates a regular user in the DB. '''

    def __init__(self, db):
        self.db = db

    def run(self):
        user_datastore.create_user(email='test@test.com', password='test')
        self.db.session.commit()


@app.route('/dummy-api/', methods=['GET'])
@http_auth_required
def dummyAPI():
    ret_dict = {
        "Key1": "Value1",
        "Key2": "value2"
    }
    return jsonify(items=ret_dict)

manager.add_command('runserver', Server(host='testflask.local', port=5000))
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db_create_reg_user', DBRegUser(db))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
