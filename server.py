from jinja2 import StrictUndefined
from flask import Flask, render_template, request
from model import connect_to_db, db, User, Response
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "SECRET"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.jinja_env.undefined = StrictUndefined



class ContactForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email("Valid email address required")])
    
    
@app.route("/")
def index_page():
    """Show homepage."""

    return render_template("index.html")


@app.route("/products")
def products_page():
    """Show products page."""

    return render_template("index.html")


@app.route("/about_us")
def about_us_page():
    """Show about_us page."""

    return render_template("about.html")


@app.route("/blog")
def blog_page():
    """Show blog page."""

    return render_template("blog.html")


@app.route("/contact")
def show_contact_form():
    """Show contact form."""

    form = ContactForm()

    return render_template("contact.html", form=form)

@app.route("/romeo")
def romeo_page():
    """Show romeo page."""

    return render_template("romeo.html")


@app.route("/contact", methods=["POST"])
def validate_contact_info():
    """validate form information"""

    form = ContactForm()
    if form.validate_on_submit():
        process_contact()
        print("Yes, it's valid")
        return render_template("contact_success.html")


def process_contact():
    """Add user question/response to database"""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    role = request.form.get("role")
    contact_reason = request.form.get("reason")
    response = request.form.get("response")

    user = User.query.filter_by(email=email).first()
    
    if not user:
        user = User(fname=fname, lname=lname, email=email, role=role, 
            contact_reason=contact_reason, response=response, entered_at=datetime.now())
        db.session.add(user)
        db.session.commit()

        new_response = Response(user_id=user.user_id, contact_reason=contact_reason, 
                                response=response, entered_at=datetime.now())
        db.session.add(new_response)
        db.session.commit()
    else: 
        new_response = Response(user_id=user.user_id, contact_reason=contact_reason, 
                                response=response, entered_at=datetime.now())
        db.session.add(new_response)
        db.session.commit()


    # else:
    #     if role and user.role != role:
    #         user.role = role
    #     if fname and user.fname != fname:
    #         user.fname = fname
    #     if lname and user.lname != lname:
    #         user.lname = lname
    #     db.session.commit()

    return 



if __name__ == "__main__":
    app.debug = True
    #connect_to_db(app)
    # DebugToolbarExtension(app)

    # PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=5000)
