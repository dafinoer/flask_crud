from wtforms import Form, StringField, PasswordField, validators, ValidationError
from .models import User
from werkzeug.security import check_password_hash

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(max=40)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
        ])
    confirm = PasswordField('Repeat Password')


    def validate_email(form, field):
        get_email = User.query.filter_by(email=field.data).first()
        if get_email is not None:
            raise ValidationError('email sudah ada')


class LoginForm(Form):
    username = StringField('username')
    password = PasswordField('password')