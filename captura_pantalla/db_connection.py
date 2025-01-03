from sqlalchemy import create_engine, Column, Integer, Float, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configuración de la conexión
DATABASE_URL = "mysql+pymysql://root:123456@localhost/test"

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Base para los modelos
Base = declarative_base()



# Crear una tabla como modelo
class ValoresCapturados(Base):
    __tablename__ = "valores_capturados"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Float)
    valor_signo = Column(Float)
    fecha_captura = Column(TIMESTAMP, default=datetime.utcnow)

# Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()



def insert_data(numbers, signed_numbers):
    """
    Inserta los números y valores con signo en la base de datos.
    :param numbers: Lista de números grandes (ej. 96,439.4)
    :param signed_numbers: Lista de valores con signos (ej. +1.32, -0.85)
    """
    try:
        for num, signo in zip(numbers, signed_numbers):
            # Crear un nuevo registro
            nuevo_valor = ValoresCapturados(
                numero=float(num.replace(',', '')),  # Convertir '96,439.4' -> 96439.4
                valor_signo=float(signo)
            )
            session.add(nuevo_valor)

        # Confirmar la transacción
        session.commit()
        print(f"{len(numbers)} registros insertados correctamente.")
    except Exception as e:
        session.rollback()  # Revertir cambios en caso de error
        print(f"Error al insertar datos: {e}")
    finally:
        session.close()

