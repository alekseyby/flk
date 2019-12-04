from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    #  We imported render_template() method from the flask framework. render_template() looks for a template (HTML file) in the templates folder.
    return render_template("home.html")
@app.route("/about)
def about():
    return render_template("about.html")
@app.route("/baam")
def salvador():
    return "Hello, Piador"


if __name__ == "__main__":
    app.run(debug=True)