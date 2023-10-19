from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos
    id = Column(Integer(), primary_key=True)
    name = Column(String(4))

# URL de conexión a la base de datos (puedes personalizarla según tu configuración)
db_url = engine ="mysql+pymysql://root:odette@127.0.0.1/monse"

engine = create_engine(db_url)

# Crea la tabla en la base de datos (si no existe)
Base.metadata.create_all(engine)