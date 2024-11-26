from flask import Blueprint, request, jsonify
from models import db, DatabaseConfig
from cryptography.fernet import Fernet

database_bp = Blueprint('database', __name__)

# Generar clave para cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@database_bp.route('', methods=['POST'])
def register_database():
    data = request.json
    encrypted_password = cipher_suite.encrypt(data['password'].encode())
    db_config = DatabaseConfig(
        host=data['host'],
        port=data['port'],
        username=data['username'],
        password=encrypted_password
    )
    db.session.add(db_config)
    db.session.commit()
    return jsonify({"id": db_config.id}), 201
