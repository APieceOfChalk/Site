from wtforms import Form, StringField, TextAreaField

class PostForm(Form):
    title = StringField('Введите своё имя:')
    body = TextAreaField('Текст:')
