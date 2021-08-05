from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    login = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class RegistrationForm(FlaskForm):
    login = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])