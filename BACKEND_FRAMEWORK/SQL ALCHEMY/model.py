from sqlalchemy import Integer,Float,String,Column

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key = True , index = True)

    name = Column(String, nullable = False)

    age = Column(Integer, nullable = False)

    course = Column(String)

    marks = Column(Integer)

