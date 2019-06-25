from flask import (Flask, request, render_template, redirect, session)
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
# from model import connect_to_db, db, 

app = Flask(__name__)
app.secret_key = "yes"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    # show homepage
    print("\n\nshow homepage\n\n")
    
    return render_template("homepage.html")
     
@app.route('/location')
def show_woods():
    """Show woods"""
    return render_template("location.html")
     
@app.route('/rsvp')
def show_tables():
    """Show tables"""
    return render_template("rsvp.html")
     
@app.route('/barinfo')
def show_smalls():
    """Show smalls"""
    return render_template("barinfo.html")
     




if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)

    #connect_to_db(app, 'postgresql:///wedding')
    app.run(host='0.0.0.0')