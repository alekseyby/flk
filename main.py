from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)

@app.route("/")
def home():
    #  We imported render_template() method from the flask framework. render_template() looks for a template (HTML file) in the templates folder.
    return render_template("home.html", title='Home')
@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/projects")
def projects():
    return render_template("projects.html", title='Projects')

@app.route("/experience")
def experience():
    return  render_template("experience.html", title='Experience')

@app.route("/designs")
def designs():
    return  render_template("designs.html", title='Designs')

@app.route("/baam")
def salvador():
    return "Hello, FooBar"


if __name__ == "__main__":
    app.run(debug=True)