from wtforms import Form, StringField, TextAreaField


class PostForm(Form):
    body = TextAreaField('Текст отзыва:')
