from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)

@app.route("/")
def home():
    #  We imported render_template() method from the flask framework. render_template() looks for a template (HTML file) in the templates folder.
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/experience")
def experience():
    return "In progress"

@app.route("/designs")
def designs():
    return "In progress"

@app.route("/baam")
def salvador():
    return "Hello, FooBar"


if __name__ == "__main__":
    app.run(debug=True)