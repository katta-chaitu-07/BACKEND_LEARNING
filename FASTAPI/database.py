from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

database_url = "postgresql://postgres:Chaitanya%4062@localhost:5432/chaitanya"

engine = create_engine(
    database_url
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)