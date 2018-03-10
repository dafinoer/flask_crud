from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from .forms import RegisterForm, LoginForm
from .models import User
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/register', methods=['GET', 'POST'])
def register_user():
    forms = RegisterForm(request.form)  
    if request.method == 'POST' and forms.validate():
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        query = User(
            username=username,
            password_hash=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8),
            email=email
        )

        db.session.add(query)

        db.session.commit()   

        flash('Check email for activate')
        return redirect(url_for('user.login_user'))

    return render_template('users/register.html', form=forms)

@user.route('/login', methods=['GET', 'POST'])
def login_user():
    forms = LoginForm(request.form)
    if request.method == 'POST' and forms.validate():
        user = request.form.get('username')
        password = request.form.get('password')

        get_query = User.query.filter_by(email=user).first()

        get_data = get_query.password_hash
        
        check_pass = check_password_hash(get_query.password_hash, password)

        if get_query.username != user and check_pass != True:
            flash('false')
        else:
            flash('thanks for login')
            return 'hallo'

    return render_template('users/login.html', form=forms)