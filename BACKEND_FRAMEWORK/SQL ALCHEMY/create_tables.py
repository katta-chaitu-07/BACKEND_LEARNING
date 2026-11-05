from model import Base
from create_engine import engine

Base.metadata.create_all(bind = engine)

print("Tables is successfully created")