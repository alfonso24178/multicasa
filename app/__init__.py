from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config.from_pyfile('../config.py')

    # Inicializar extensiones
    db.init_app(app)
    csrf.init_app(app)

    # Importar rutas
    from app.routes.main import main
    app.register_blueprint(main)

    return app