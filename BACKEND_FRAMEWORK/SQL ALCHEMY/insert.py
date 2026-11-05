from create_session import SessionLocal

from model import student

db = SessionLocal()

new_student = student(
    id = 2,
    name = "Rahul",
    age = 22,
    course = "Python",
    marks = 96
)

db.add(new_student)

db.commit()

db.close()