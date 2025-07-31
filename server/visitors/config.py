from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://@PC-T02/QuikTrip?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

Session = sessionmaker(bind=engine)

#Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

