from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://mudassar_sit722_part3_user:gr2F32IrESvncwp8Na7MOpIwqd0qz8fR@dpg-crs09n0gph6c738n26g0-a.oregon-postgres.render.com/mudassar_sit722_part3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
