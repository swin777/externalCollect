from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:1234@localhost:5432/external_db')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

base = declarative_base()



