from wtforms import Form, StringField, PasswordField, validators

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(max=40)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
        ])
    confirm = PasswordField('Repeat Password')
