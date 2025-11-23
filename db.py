# db.py
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",      # el host donde expusiste PostgreSQL
        port=5437,             # el puerto mapeado de tu Docker
        database="tienda",       # POSTGRES_DB en tu compose
        user="admin",          # POSTGRES_USER
        password="admin123"     # POSTGRES_PASSWORD
    )