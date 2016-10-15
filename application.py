from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_form():
    """Shows the application form."""

    return render_template("application-form.html")

@app.route("/application-response", methods=["POST"])
def application_response():
    """Confirm application receipt and thank applicant."""

    name = request.form.get("first-name") + " " + request.form.get("last-name")
    salary = request.form.get("salary")
    role = request.form.get("role")

    return render_template("application-response.html", 
                           name=name, salary=salary, role=role)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

