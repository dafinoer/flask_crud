import os
from flask import Flask
from flask import render_template


config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'config.py')


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_path[config_name])
    # app.config.from_pyfile(str(config_path))

    from app.user.view import user

    app.register_blueprint(user)

    @app.route('/')
    def home_hello():
        context = {
            'title':'this is flask',
            'body':'body'
        }
        return render_template('base.html', result=context, name='hallo')

    return app
