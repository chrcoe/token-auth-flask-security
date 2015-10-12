'''
Setup API specific settings.
'''

from flask import Flask
from models import User, Role
from flask.ext.sqlalchemy import SQLAlchemy, SQLAlchemyUserDatastore
from flask.ext.security import Security
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])
db = SQLAlchemy()

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create a user to test with


@app.before_first_request
def create_user():
    db.create_all()
    if not User.query.first():
        user_datastore.create_user(
            email='test@example.com', password='test123'
        )
        db.session.commit()

if __name__ == '__main__':
    app.run()
