import os
from app import create_app
from flask_sqlalchemy import SQLAlchemy


config_name = os.getenv('FLASK_CONFIG')
app = create_app()

if __name__ == 'main':
    app.run()
