import os

# Clave secreta para formularios
SECRET_KEY = 'clave-super-secreta'

# Configuración de la base de datos (ajusta tus datos si cambian)
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'multicasa'

# Para usar SQLAlchemy con MySQL
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/multicasa'
SQLALCHEMY_TRACK_MODIFICATIONS = False
