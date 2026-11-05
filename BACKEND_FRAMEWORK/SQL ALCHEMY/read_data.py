from model import Base,student

from create_session import SessionLocal

db = SessionLocal()

data = db.query(student).filter(student.id == 10).first()


if data : 
    print(f"Id : {data.id}")
    print(f"name : {data.name}")

else :

    print("Student not found")    

    

db.close()