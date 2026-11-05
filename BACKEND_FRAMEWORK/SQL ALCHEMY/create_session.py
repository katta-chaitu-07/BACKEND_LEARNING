from sqlalchemy.orm import sessionmaker
from create_engine import engine

SessionLocal = sessionmaker(bind = engine)

