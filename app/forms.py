from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_security.forms import RegisterForm, Required


class ConsultForm(Form):
    name = StringField('Введите своё имя:', validators=[DataRequired()])
    mobile = StringField('Ваш номер телефона::', validators=[DataRequired()])


class ExtendedRegisterForm(RegisterForm):
    name = StringField('Имя', [Required()])


