from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{user}:{password}@{host}:3306/{db}".format(
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASS"),
    host=os.environ.get("MYSQL_HOST"),
    db=os.environ.get("MYSQL_NAME"),
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_timeout=5, pool_recycle=4)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
