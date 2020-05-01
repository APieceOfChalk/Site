from wtforms import Form, StringField
from wtforms.validators import DataRequired


class ConsultForm(Form):
    name = StringField('Введите своё имя:', validators=[DataRequired()])
    mobile = StringField('Ваш номер телефона::', validators=[DataRequired()])
