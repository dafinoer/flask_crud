from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from .forms import RegisterForm, LoginForm

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/register', methods=['GET', 'POST'])
def register_user():
    forms = RegisterForm(request.form)  
    if request.method == 'POST' and forms.validate():
        flash('Thanks for registering')
        return redirect(url_for('home_hello'))

    return render_template('users/register.html', form=forms)

@user.route('/login', methods=['GET', 'POST'])
def login_user():
    forms = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('thanks for login')
        return 'hallo'
    

    return render_template('users/home.html', form=forms)