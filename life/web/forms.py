from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField #PasswordField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    genre = SelectField('種類', choices=[('Todo', 'Todo'), ('Schedule', 'Schedule')])
    title = StringField('やること', validators=[DataRequired()])
    body = StringField('内容(任意)')
    date = DateField('期限', format="%Y-%m-%d")
    submit = SubmitField('登録')

"""
class UserForm(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired()])
    password = PasswordField('パスワード', validators=[DataRequired()])
    submit = SubmitField('登録')
"""