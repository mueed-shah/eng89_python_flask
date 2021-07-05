# Installing flask

from flask import Flask, redirect, url_for, render_template

# create object of this class

app = Flask(__name__)  # creating an app instance


# create func to link to homepage
# create function to browser
@app.route("/")  # decorating our function with @app.route  to set route in browser
def index():
    return " Welcome to DevOps Eng 89 DevOps team"


# create a welcome page
@app.route("/welcome/")  # best practice to have / at end to load page for both cases
def welcome():
    return render_template("welcome.html")

@app.route("/<username>/") # passing variable provided by the user in the browser
def greet_user(username):
    return f"Welcome to flask web app dear {username}" # display the name back to user in the browsser


# create a decorator to route traffic to login page
# display 2 messages of your choice in form of h1 and h2
@app.route("/login/")
def login():  # redirect, url_for needs to be imported to redirect users
    return redirect(url_for("welcome"))  # Redirect user to welcome page


# to fix error we need to create folder called templates
# project folder
# templates folder
# welcome.html

# app.py


if __name__ == "__main__":
    app.run(debug=True)
