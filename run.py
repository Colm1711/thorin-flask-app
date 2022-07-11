import os
from flask import Flask, render_template

# creating an instance of this and storing it in app
# naming convention in flask is to call it app
# first arg is the name of the module(__name__ which is built in var of Python)
app = Flask(__name__)

# using the app.route decorator
# this function is called a view or routing
# when we go to the top level of our domain with "/" it binds index to itself
@app.route("/")
def index():
    # flask expects this index.html to be in the templates folder with an s
    return render_template("index.html")


# creating another route/view function for about page
@app.route("/about")
def about():
    return render_template("about.html")


# creating another route/view function for about page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# referencing the os import using the get method
# os module gets the IP module if it exists and sets 0.0.0.0 if it dosen't exist
# doing the same with port, using the 5000 as this is the common one used by flask
# setting debug to True to help with our debug, this is should be set for production code or submitting project

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)