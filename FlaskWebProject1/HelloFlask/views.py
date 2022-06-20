from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
        message = "Hello, Flask ",
        content = formatted_now)


@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')

@app.route('/about')
def about():
    return render_template(
        "about.html",
        title = "About HelloFlask", 
        content = "Example app page for Flask. ")

@app.route('/contact_us')
def contact_us():
    return render_template(
        "contact_us.html",
        title = "Contact the developers",
        content1 = "Ryan Lance",
        content2 = "Email: ryan.lance.3141@gmail.com")
