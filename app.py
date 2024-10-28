import flask

# ----------------------------------------------------------------------

app = flask.Flask(__name__, template_folder="./templates")


# ----------------------------------------------------------------------

@app.route("/", methods=["GET"])
def index():
    # render homepage html 
    html_code = flask.render_template("index.html")
    response = flask.make_response(html_code)

    return response