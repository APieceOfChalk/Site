from app import app
from flask import render_template
from flask import redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/')
def register():
    return redirect(url_for('security.register'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


