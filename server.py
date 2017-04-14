from flask import Flask, render_template, request
from model import connect_to_db, db, User, Response
from datetime import datetime

app = Flask(__name__)

app.secret_key = "SECRET"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


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

    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def process_contact():
    """Show contact form."""

    email = request.form.get("email")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    phone = request.form.get("phone")
    role = request.form.get("role")
    interested_in = request.form.get("interested_in")
    is_beta_tester = request.form.get("beta_tester")
    is_subscriber = request.form.get("newsletter")
    response = request.form.get("response")

    user = User.query.filter_by(email=email).first()
    
    if not user:
        user = User(fname=fname, lname=lname, email=email, phone=phone, role=role, 
            is_beta_tester=is_beta_tester, is_subscriber=is_subscriber, entered_at=datetime.now())
        db.session.add(user)
        db.session.commit()
    else:
        if newsletter and user.newsletter != newsletter:
            user.newsletter = newsletter
        if beta_tester and beta_tester != beta_tester:
            user.beta_tester = beta_tester
        if role and user.role != role:
            user.role = role
        if fname and user.fname != fname:
            user.fname = fname
        if lname and user.lname != lname:
            user.lname = lname
        db.session.commit()

    if interested_in or response:
        new_response = Response(user_id=user.user_id, type_response=interested_in, 
                                response=response, entered_at=datetime.now())
        db.session.add(new_response)
        db.session.commit()

    return render_template("contact.html")


# @app.route("/romeo")
# def romeo_page():
#     """Show romeo page."""

#     return render_template("romeo.html")

if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    # DebugToolbarExtension(app)

    # PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=5000)