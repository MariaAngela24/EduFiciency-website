from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User model."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    email = db.Column(db.String(30), nullable=False, unique=True)
    role = db.Column(db.String(100))
    comment_question = db.Column(db.Text)
    feedback = db.Column(db.Text)
    beta_tester = db.Column(db.Boolean)
    newsletter = db.Column(db.Boolean)
    responses = db.relationship('Response', backref='user')
    entered_at = db.Column(db.DateTime)

    def __repr__(self):
        return "<User id=%s, email=%s>" % (self.user_id, self.email)

class Response(db.Model):
    """User response table."""

    response_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    type_response = db.Column(db.String(100))
    response = db.Column(db.Text)
    entered_at = db.Column(db.DateTime)
    responded_to = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User email=%s, response=%s>" % (self.user_id.email, self.response)

def init_app():
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app, db_uri='postgres:///courses'):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
