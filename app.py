from flask import Flask
from flask import render_template

import re
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():    
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    
    return render_template(
        "hello_there.html",
        name = name,
        date = datetime.now()
    )

# send a static JSON file
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/hello/<name>/<age>")
def hello_there_age(name, age):
    now = datetime.now()
    formatted_now = now.strftime("%A, %B %d, %Y at %X")

    # get letters only using regex
    # restrict to alphanumeric only
    # (this will help prevent XSS attacks)

    regex_match = re.match("[a-zA-Z]+", name)

    age = int(float(age))

    if regex_match and int(age) == age:
        clean_name = regex_match.group(0)
        clean_age = str(age)
    elif regex_match and int(age) != age:
        clean_name = regex_match.group(0)
        clean_age = 'some'
    else:
        clean_name = "friend"

        if int(age) == age:
            clean_age = str(age)
        else:
            clean_age = 'some'


    content = "Hi there, " + clean_name + "! It's " + formatted_now + " and you're " + clean_age + " years old!"

    # print a URL for easy access from the Python Debug Console
    print("http://127.0.0.1:5000/hello/" + clean_name)

    return content