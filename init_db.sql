CREATE DATABASE scanner_db;

USE scanner_db;

CREATE TABLE database_config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    host VARCHAR(255) NOT NULL,
    port INT NOT NULL,
    username VARCHAR(255) NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE scan_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    database_id INT NOT NULL,
    table_name VARCHAR(255) NOT NULL,
    column_name VARCHAR(255) NOT NULL,
    classification VARCHAR(255) NOT NULL,
    FOREIGN KEY (database_id) REFERENCES database_config(id)
);
