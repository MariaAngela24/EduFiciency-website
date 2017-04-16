from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User model."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    role = db.Column(db.String(100))
    contact_reason = db.Column(db.String(200))
    response = db.Column(db.String(10000))

    responses = db.relationship('Response', backref='user')
    entered_at = db.Column(db.DateTime)

    def __repr__(self):
        return "<User id=%s, email=%s>" % (self.user_id, self.email)


class Response(db.Model):
    """User response table."""

    __tablename__ = "responses"

    response_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    contact_reason = db.Column(db.String(100))
    response = db.Column(db.Text)
    responded_to = db.Column(db.Boolean, default=False)
    responded_at = db.Column(db.DateTime)
    entered_at = db.Column(db.DateTime)

    def __repr__(self):
        return "<User email=%s, response=%s>" % (self.user_id.email, self.response)


def init_app():
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)


def connect_to_db(app, db_uri='postgres:///contacts'):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
