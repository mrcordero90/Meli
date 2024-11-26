project/
│
├── app.py                # Archivo principal de la aplicación
├── models.py             # Definición de modelos y base de datos
├── routes/               # Endpoints de la API
│   ├── database.py
│   └── scan.py
├── requirements.txt      # Dependencias del proyecto
├── Dockerfile            # Archivo Docker para contenerizar la aplicación
├── init_db.sql           # Script SQL para inicializar la base de datos
└── README.md             # Documentación del proyecto


Configuracion

1 - Clonar el repositorio 
git clone https://github.com/mrcordero90/Meli.git
cd Meli

2 - Instalar dependencias
pip install -r requirements.txt

3 - Inicializar la BD
mysql -u root -p < init_db.sql

4 - Ejecutar la aplicacion

python app.py

5 - Registrar una BD

POST /api/v1/database

6

Escanear una Base de Datos
Endpoint:
POST /api/v1/database/scan/:id

Parámetro:
id: ID de la base de datos registrada.

Respuesta Exitosa:


{
  "message": "Scan completed"
}

7- Obtener resultados del scanneo
GET /api/v1/database/scan/:id

Respuesta

{
  "users": [
    {
      "column_name": "username",
      "classification": "USERNAME"
    },
    {
      "column_name": "email",
      "classification": "EMAIL_ADDRESS"
    }
  ],
  "transactions": [
    {
      "column_name": "credit_card",
      "classification": "CREDIT_CARD_NUMBER"
    }
  ]
}
