from sqlalchemy import create_engine, Column, Integer, DECIMAL, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pytz


# Configuración de la conexión
DATABASE_URL = "mysql+pymysql://root:123456@localhost/test"

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Base para los modelos
Base = declarative_base()


# Configurar la zona horaria
timezone = pytz.timezone("Europe/Madrid")


# Función para obtener la hora local
def get_local_time():
    return datetime.now(timezone)


# Crear una tabla como modelo
class ValoresCapturados(Base):
    __tablename__ = "valores_capturados"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(DECIMAL(10, 2))  # Usamos DECIMAL(10,2)
    valor_signo = Column(DECIMAL(10, 2))  # También DECIMAL(10,2)
    fecha_captura = Column(TIMESTAMP, default=get_local_time)

# Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()



def insert_data(number, signed):
    """
    Inserta los números y valores con signo en la base de datos.
    :param number: Número grande en formato de texto (ej. '96,439.4')
    :param signed: Valor con signo en formato de texto (ej. '+1.32', '-0.85')
    """
    try:

        #print(f"{number} - {signed}")

        # Validar y limpiar los datos
        #if not number or not signed:
        #    raise ValueError("Los valores no pueden estar vacíos.")

        # Remover comas y convertir a float
        #cleaned_number = float(number)
        #cleaned_signed = float(signed)


        # Crear un nuevo registro
        nuevo_valor = ValoresCapturados(
            numero=float(number),
            valor_signo=float(signed)
        )
        session.add(nuevo_valor)

        # Confirmar la transacción
        session.commit()
        print(f"Registro insertado correctamente: {number}, {signed}")
    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except Exception as e:
        session.rollback()  # Revertir cambios en caso de error
        print(f"Error al insertar datos: {e}")
    finally:
        session.close()