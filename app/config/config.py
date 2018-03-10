DEBUG = True

SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

DB_URI = 'postgresql://{db_user}:{db_pass}@{db_port}/{db_database}'.format(
    db_user='postgres',
    db_pass='sayursop123',
    db_port='localhost',
    db_database='flask_crud'
)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False


