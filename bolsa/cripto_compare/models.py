from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
DATABASE_URL = "mysql+pymysql://root:123456@localhost/test_datatable"

# Configuración del motor y sesión
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


# Models
class CryptoPrice(Base):
    __tablename__ = "cripto_prices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String(200), nullable=False)
    symbol = Column(String(200), nullable=False)
    price = Column(DECIMAL(11,2), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)



def init_db():
    Base.metadata.create_all(engine)

