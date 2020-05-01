from app import app
from flask import render_template

from forms import ConsultForm

from flask import request
from app import db

from flask import redirect
from flask import url_for

from models import Consultation

from wtforms import ValidationError

@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/note', methods=['POST', 'GET'])
def note():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        try:
            number = Consultation(name=name, mobile=mobile)
            db.session.add(number)
            db.session.commit()
        except:
            print('Что-то пошло не так!')
        return redirect(url_for('success'))

    form = ConsultForm()
    return render_template('note.html', form=form)


@app.route('/note/success')
def success():
    return render_template('success.html')
