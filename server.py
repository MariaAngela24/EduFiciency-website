from flask import Flask, render_template

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

    return render_template("products.html")


@app.route("/about_us")
def about_us_page():
    """Show about_us page."""

    return render_template("about_us.html")


@app.route("/blog")
def blog_page():
    """Show blog page."""

    return render_template("blog.html")


@app.route("/contact")
def contact_page():
    """Show contact page."""

    return render_template("contact.html")

if __name__ == "__main__":
    app.debug = True

    # DebugToolbarExtension(app)

    # PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=5000)