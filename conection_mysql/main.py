from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Configuración base
DATABASE_URL = "mysql+pymysql://root:123456@localhost/gtank"

# Crear motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear una fábrica de sesiones
Session = sessionmaker(bind=engine)

# Base para modelos
Base = declarative_base()


# Modelo de la tabla vat_types
class VatType(Base):
    __tablename__ = 'vat_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    country_code = Column(String(4), nullable=False, default='')
    year = Column(String(4), nullable=False)
    vat_tax = Column(DECIMAL(8, 2), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=True)



# Función para listar los registros de vat_types
def listar_vat_types():
    session = Session()
    try:
        # Consultar los registros
        vat_types = session.query(VatType).all()
        for vat_type in vat_types:
            print(
                f"ID: {vat_type.id}, Country Code: {vat_type.country_code}, "
                f"Year: {vat_type.year}, VAT Tax: {vat_type.vat_tax}, "
                f"Created At: {vat_type.created_at}, Updated At: {vat_type.updated_at}"
            )
    finally:
        session.close()




if __name__ == "__main__":
    listar_vat_types()