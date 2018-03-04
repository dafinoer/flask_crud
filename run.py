import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
print(config_name)
app = create_app(config_name)

if __name__ == 'main':
    app.run()

