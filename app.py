from flask import Flask
from models import db
from routes.database import database_bp
from routes.scan import scan_bp

# Inicialización de Flask
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/scanner_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos
db.init_app(app)

# Registro de Blueprints
app.register_blueprint(database_bp, url_prefix='/api/v1/database')
app.register_blueprint(scan_bp, url_prefix='/api/v1/database/scan')

if __name__ == '__main__':
    app.run(debug=True)
