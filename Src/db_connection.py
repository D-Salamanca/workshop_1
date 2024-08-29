from sqlalchemy import create_engine
from decouple import config

# Configuración de la cadena de conexión a PostgreSQL
engine = create_engine(f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_DB')}")

class DbConnection:
    def __init__(self, eng=engine):
        self.engine = eng

# Instancia de la conexión
conn = DbConnection()

# Prueba de la conexión
if __name__ == "__main__":
    try:
        with conn.engine.connect() as connection:
            print("Conexión exitosa a la base de datos.")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
