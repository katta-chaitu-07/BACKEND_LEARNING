from sqlalchemy import create_engine

engine = create_engine("sqlite:///practice.db")

with engine.connect() as connection:
    print("Database connected successfully!")