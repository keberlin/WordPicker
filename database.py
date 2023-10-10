from flask_sqlalchemy import SQLAlchemy

WORDPICKER_DB_URI = "postgresql://postgres:postgres@localhost:5432/wordpicker"

db = SQLAlchemy()
