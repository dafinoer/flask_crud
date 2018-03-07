from flask import Flask, Blueprint, render_template
from .forms import RegisterForm

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/register')
def register_user():
    form = RegisterForm()

    return render_template('users/register.html')
