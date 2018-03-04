from flask import Flask, Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/register')
def register_user():
    return render_template('users/register.html')