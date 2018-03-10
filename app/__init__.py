import os
from flask import Flask
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'config.py')
db =SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_settings[config_name])
    app.config.from_pyfile(str(config_path))

    #database
    # app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URI
    # print('URI > ',Config.DB_URI) 
    
    # app.config['SECRET_KEY'] = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

    csrf = CSRFProtect()
    csrf.init_app(app)


    db.init_app(app)




    from app.user.view import user
    from app.home.view import homes

    app.register_blueprint(homes)
    app.register_blueprint(user)

    
    return app
