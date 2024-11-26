from flask import Blueprint, jsonify, request
from models import db, DatabaseConfig, ScanResult
import pymysql
import re

scan_bp = Blueprint('scan', __name__)

PATTERNS = {
    "USERNAME": r"(?i)username",
    "EMAIL_ADDRESS": r"(?i)email",
    "CREDIT_CARD_NUMBER": r"(?i)credit_card|cc_number",
}

def classify_column(column_name):
    for classification, pattern in PATTERNS.items():
        if re.search(pattern, column_name):
            return classification
    return "N/A"

@scan_bp.route('/<int:id>', methods=['POST'])
def scan_database(id):
    db_config = DatabaseConfig.query.get_or_404(id)
    decrypted_password = cipher_suite.decrypt(db_config.password.encode()).decode()

    # Conexión a la base de datos objetivo
    connection = pymysql.connect(
        host=db_config.host,
        user=db_config.username,
        password=decrypted_password,
        port=db_config.port
    )
    cursor = connection.cursor()

    # Obtener estructura de la base de datos
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    for (table,) in tables:
        cursor.execute(f"DESCRIBE {table}")
        columns = cursor.fetchall()
        for column in columns:
            column_name = column[0]
            classification = classify_column(column_name)
            result = ScanResult(
                database_id=id,
                table_name=table,
                column_name=column_name,
                classification=classification
            )
            db.session.add(result)
    db.session.commit()
    return jsonify({"message": "Scan completed"}), 201

@scan_bp.route('/<int:id>', methods=['GET'])
def get_scan_results(id):
    results = ScanResult.query.filter_by(database_id=id).all()
    output = {}
    for result in results:
        if result.table_name not in output:
            output[result.table_name] = []
        output[result.table_name].append({
            "column_name": result.column_name,
            "classification": result.classification
        })
    return jsonify(output), 200
