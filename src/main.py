from fastapi import Depends, FastAPI, Response, status, HTTPException
from . import model, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

model.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def say_hello():
    return {"Hello": "Van"}


@app.get("/student/{id}")
async def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(model.Student).filter(model.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with the {id} is not found")
    return student


@app.post("/add/student", status_code=status.HTTP_201_CREATED)
async def add_student(student: schemas.StudentModel, db: Session = Depends(get_db)):
    new_student = model.Student(
        first_name=student.first_name, last_name=student.last_name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.delete("/student/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(model.Student).filter(model.Student.id == id)

    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with the {id} is not found")
    
    student.delete(synchronize_session=False)
    db.commit()
    return {'message': f"Student with {id} has been deleted"}

@app.get("/students")
async def get_all_students(db: Session = Depends(get_db)):
    students = db.query(model.Student).all()
    return students

@app.put("/update/{id}")
async def update_student(id: int, student: schemas.StudentModel, db: Session = Depends(get_db)):
    old_info_student = db.query(model.Student).filter(model.Student.id == id)

    if not old_info_student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with the {id} is not found")
    
    print(type(student))
    # old_info_student.update({"first_name": "Jason"})
    old_info_student.update(dict(student))
    db.commit()
    return {'message': f"Student with {id} has been updated"}
