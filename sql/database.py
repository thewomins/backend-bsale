from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

values = dotenv_values(".env")

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{user}:{password}@{host}:3306/{db}".format(
    user=values.get("MYSQL_USER"),
    password=values.get("MYSQL_PASS"),
    host=values.get("MYSQL_HOST"),
    db=values.get("MYSQL_NAME"),
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_timeout=5, pool_recycle=4)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
