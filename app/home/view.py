from flask import render_template, Blueprint

homes = Blueprint('homes', __name__)

@homes.route('/')
def home_hello():
    context = {
        'title':'this is flask',
        'body':'body'
    }
    return render_template('users/home.html', result=context, name='hallo')