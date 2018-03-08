

class Config(object):
    """
    """
    TESTING = False
    DB_URI = 'postgresql://{db_user}:{db_pass}@{db_port}/{db_database}'.format(
        db_user='postgres',
        db_pass='sayursop123',
        db_port='localhost',
        db_database='flask_crud'
    )

class ConfigDevelopment(Config):
    DEBUG = True
    print('debug')

class ConfigProduction(Config):
    DEBUG = False

app_settings = {
    'development': ConfigDevelopment,
    'production': ConfigProduction
}


