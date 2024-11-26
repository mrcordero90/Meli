from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DatabaseConfig(db.Model):
    __tablename__ = 'database_config'
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(255), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.Text, nullable=False)

class ScanResult(db.Model):
    __tablename__ = 'scan_results'
    id = db.Column(db.Integer, primary_key=True)
    database_id = db.Column(db.Integer, db.ForeignKey('database_config.id'), nullable=False)
    table_name = db.Column(db.String(255), nullable=False)
    column_name = db.Column(db.String(255), nullable=False)
    classification = db.Column(db.String(255), nullable=False)
